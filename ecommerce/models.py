from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings

from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(
        User, related_name="user_cart", on_delete=models.CASCADE
    )
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, blank=True, null=True
    )


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_item", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="cart_product", on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=1)