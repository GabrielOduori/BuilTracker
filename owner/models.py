from django.db import models
from constructor.models import Constructor
from 
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
    
    
class Profile(models.Model):
    project_owner = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profiles',default='profile.jpg')
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
     
    @receiver(post_save, sender=User) 
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()  
    
