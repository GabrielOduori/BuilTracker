from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User

class FinancierSignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_financier = True
        user.save()
        financier =       