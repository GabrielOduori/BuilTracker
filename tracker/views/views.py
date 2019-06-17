from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth

# Create your views here.
def index(request):
    
    return render(request,'index.html') 

def create_wallet(request):
    
    return render(request,'financier.html')


def view_wallet(request):
    
    return render(request,'owner.html')

