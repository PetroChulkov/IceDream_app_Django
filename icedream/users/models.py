from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    house = models.CharField(max_length=50, null=False)
    postal_code = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

