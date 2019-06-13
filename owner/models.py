from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    totalcost = models.PositiveIntegerField(default=0)
    constructor = models.OneToOneField(Constructor,on_delete=models.CASCADE,blank=False)
    startdate = models.DateField()
    enddate = models.DateField() 
    wallet = models.OneToOneField(Wallet,on_delete=models.CASCADE)
    workers = models.PositiveIntegerField(default=0)  
    
    
    def __str__(self):
        return self.name
