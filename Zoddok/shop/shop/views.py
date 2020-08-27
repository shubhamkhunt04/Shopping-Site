from django.shortcuts import render
from urllib import request

#home page view
def home(request):
    return render(request,'index.html')