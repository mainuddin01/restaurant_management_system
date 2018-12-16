from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class RestaurantUserManager(UserManager):
    pass

class RestaurantUser(AbstractUser):
    objects = RestaurantUserManager()
