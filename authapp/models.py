from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def basket_price(self):
        return sum(el.product_cost for el in self.basket.all())

    def basket_quantity(self):
        return sum(el.quantity for el in self.basket.all())
