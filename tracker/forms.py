from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User,Financier,Owner

class FinancierSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_financier = True
        user.save()
        financier =  Financier.objects.create(user=user) 
        return user 
    
class OwnerSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_owner = True
        user.save()
        owner = Owner.objects.create(user=user) 
        return user 
        