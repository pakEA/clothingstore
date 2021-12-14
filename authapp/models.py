from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)
