from django.shortcuts import render, redirect
from urllib import request
from products.models import Category
import json
from products.views import get_categories

#home page view
def home(request):
    jsonTree=get_categories()
    context={
        'category':json.loads(jsonTree),
    }
    return render(request,'index.html',context)

#invalid url page view
def invalid_url_view(request):
    jsonTree=get_categories()
    context={
        'category':json.loads(jsonTree),
    }
    return render(request,'invalid_url.html',context=context)