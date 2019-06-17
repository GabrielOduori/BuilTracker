from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth
from ..decorators import owner_required,financier_required
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    return render(request,'index.html') 

@financier_required
@login_required
def create_wallet(request):
    
    return render(request,'financier.html')

@owner_required
@login_required
def view_wallet(request):
    
    return render(request,'owner.html')

