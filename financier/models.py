from django.db import models

# Create your models here.

class Financier(models.Model):
    name = models.CharField(max_length=200)
    wallet = models.OneToOneField(Wallet,on_delete=models.CASCADE,blank=False)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,blank=False)
    
    def __str__(self):
        return self.name
