from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_financier = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    



