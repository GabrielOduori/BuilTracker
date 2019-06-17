from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth

# Create your views here.
def index(request):
    
    consumer_key = "gzAz06Sj8uOVgD7ACMfGlAEEFdIQ87Cs"
    consumer_secret = "BQnGd8JrDM5e795n"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    print (r.text)
    
    return render(request,'index.html')