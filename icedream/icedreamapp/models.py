from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class IceCream(models.Model):
    CHOICE = (
        ('Ice Cream', ('Ice Cream')),
        ('Sorbet', ('Sorbet')),
        ('Vegan', ('Vegan')),
        ('Cone/Box', ('Cone/Box')),
    )
    name = models.CharField(max_length=50, null=False, unique=True)
    compound = models.CharField(max_length=150, null=False)
    calories = models.CharField(max_length=25, null=False)
    proteins = models.CharField(max_length=25, null=False)
    carbonhydrates = models.CharField(max_length=25, null=False)
    fats = models.CharField(max_length=25, null=False)
    price = models.FloatField(default=0)
    size = models.CharField(max_length=50, null=False, unique=False)
    rating = models.IntegerField(default=0)
    special = models.BooleanField(default=False)
    type = models.CharField(max_length=32,
       choices=CHOICE,
       default='IceCream'
   )
    image = CloudinaryField('image', default='image')

    def __str__(self):
        return f"{self.name}"

class CheckoutInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    shipping_option = models.CharField(max_length=20)
    message = models.TextField()

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(IceCream, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total = models.FloatField(default=0)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(IceCream, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

User.profile = property(lambda u: IceCream.objects.get_or_create(user=u)[0])
User.cart = property(lambda u: Cart.objects.get_or_create(user=u)[0])


