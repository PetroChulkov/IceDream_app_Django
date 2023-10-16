from django.urls import path
from . import views

app_name = 'icedreamapp'

urlpatterns = [
    path("", views.index, name="index"),
    path('flavors/', views.flavors, name='flavors'),
    path('about/', views.about, name='about'),
    path('detail/<str:marker>/<int:product_id>/', views.detail, name='detail'),
    path('add-to-cart/<str:marker>/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<str:marker>/<int:product_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('cart/', views.view_cart, name='cart'),
    path('increase-cart-item/<int:product_id>/', views.increase_cart_item, name='increase-cart-item'),
    path('decrease-cart-item/<int:product_id>/', views.decrease_cart_item, name='decrease-cart-item'),
    path('contact', views.contact, name='contact'),
    path('contact/success', views.contact_success, name='contact-success'),
    path('checkout/', views.view_checkout, name='checkout'),
]