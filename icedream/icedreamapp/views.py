from django.shortcuts import render, get_object_or_404, redirect
from .models import IceCream, Cart, CartItem, ConeBox
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from django.db.models import F, Sum
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    products = IceCream.objects.filter(special=True)
    return render(request, 'icedreamapp/index.html', {"products": products})

def flavors(request):
    products = IceCream.objects.all()
    boxes = ConeBox.objects.all()
    return render(request, 'icedreamapp/flavors.html', {"products": products, "boxes": boxes})

def about(request):
    return render(request, 'icedreamapp/about.html')

def detail(request, marker, product_id):
    if marker == 'icecream':
        product = get_object_or_404(IceCream, pk=product_id)
    else:
        product = get_object_or_404(ConeBox, pk=product_id)
    return render(request, 'icedreamapp/product.html', {"product": product})


@login_required(login_url='login')
def add_to_cart(request, marker, product_id):
    if marker == 'icecream':
        product = IceCream.objects.get(pk=product_id)
    else:
        product = ConeBox.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    price = cart_item.product.price
    print(price)
    cart_item.total = price
    cart_item.save()
    cart.save()

    if not item_created:
        quantity = cart_item.quantity + 1
        price = quantity * cart_item.product.price
        print(price)
        cart_item.total = price
        cart_item.quantity = quantity
        cart_item.save()

    return redirect('icedreamapp:flavors')


@login_required(login_url='login')
def remove_from_cart(request, marker, product_id):
    if marker == 'icecream':
        product = IceCream.objects.get(pk=product_id)
    else:
        product = ConeBox.objects.get(pk=product_id)
    cart = Cart.objects.get(user=request.user)
    try:
        cart_item = cart.cartitem_set.get(product=product)
        if cart_item.quantity >= 1:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect('icedreamapp:cart')

@login_required(login_url='login')
def view_cart(request):
    cart = request.user.cart
    user_id = request.user.id
    cart_items = CartItem.objects.filter(cart=cart)
    sum = CartItem.objects.filter(cart=cart).aggregate(Sum('total'))
    count = CartItem.objects.filter(cart=cart).count()
    return render(request, 'cart.html', {'cart_items': cart_items, 'sum':sum, 'count':count})

@login_required(login_url='login')
def increase_cart_item(request, product_id):
    product = IceCream.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    cart_item.quantity += 1
    price = cart_item.quantity * cart_item.product.price
    cart_item.total = price
    cart_item.save()

    return redirect('icedreamapp:cart')

@login_required(login_url='login')
def decrease_cart_item(request, product_id):
    product = IceCream.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item = cart.cartitem_set.get(product=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        price = cart_item.quantity * cart_item.product.price
        cart_item.total = price
        cart_item.save()
    else:
        cart_item.total = 0
        cart_item.delete()

    return redirect('icedreamapp:cart')

def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data['message']
            print(message)
            try:
                send_mail(subject, message, from_email, ["icedreamt@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("icedreamapp:contact-success")
    return render(request, "contact.html", {"form": form})


def contact_success(request):
    return render(request, 'icedreamapp/success.html')

@login_required(login_url='login')
def view_checkout(request):
    cart = request.user.cart
    user_id = request.user.id
    cart_items = CartItem.objects.filter(cart=cart)
    sum = CartItem.objects.filter(cart=cart).aggregate(Sum('total'))
    count = CartItem.objects.filter(cart=cart).count()
    return render(request, 'checkout.html', {'cart_items': cart_items, 'sum':sum, 'count':count})