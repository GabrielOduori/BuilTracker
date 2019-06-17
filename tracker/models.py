from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    is_financier = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    


class Financier(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
class Owner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


