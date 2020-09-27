import os
from django import template
from products.views import get_categories
import json
from products.models import Category
import urllib.parse as urlparse
from urllib.parse import urlencode
import string
from shop.models import Team
register = template.Library()


@register.simple_tag
def get_team():
    return Team.objects.all()

@register.simple_tag
def get_env_var(key):
    return os.environ.get(key)

@register.filter(name='times') 
def times(number):
    return range(len(number))

@register.filter(name='var_length') 
def var_length(number):
    return (len(number)-1)

@register.simple_tag
def get_node_value(node_list,index):
    return node_list[index]

@register.simple_tag
def get_node_url(node_list,index):
    node=get_node_value(node_list,index)
    return node.get_absolute_url()

@register.simple_tag
def get_category(category_id):
    category=Category.objects.get(pk=category_id)
    return category.get_absolute_url()

@register.simple_tag(takes_context = True)
def query_transform(context,url,param_name,param_value):
    if '?' in url:
        if param_name in url:
           return query_transform_with_cust_url(url,param_name,param_value)
        else:
            return url+"&"+param_name+"="+param_value
    else:
        return url+"?"+param_name+"="+param_value

@register.simple_tag(takes_context = True)
def query_transform_with_cust_url(url,param_name,param_value):
    url=url.split("?")
    url2=url[1].split("&")
    new_url='?'
    i=0
    max_len_url=len(url2)-1
 
    for x in url2:
        splited=x.split("=")
        
        if splited[0] == param_name:
            x=splited[0]+"="+param_value

        if i == max_len_url:
            new_url+=x
        else:
            new_url+=x+"&"
        i+=1

    return new_url

@register.simple_tag()
def remove_to(url,param_name):
    url=url.split("?")
    url2=url[1].split("&")
    new_url='?'
    i=0
    max_len_url=len(url2)-1
 
    for x in url2:
        splited=x.split("=")
        
        if splited[0] == param_name:
            if i == max_len_url:
                new_url=new_url[:-1]
            i+=1
            continue
        else:
            x=splited[0]+"="+splited[1]
        
        if i == max_len_url:
            new_url+=x
        else:
            new_url+=x+"&"
        i+=1    
    return new_url

@register.inclusion_tag('nav.html')
def show_categories():
      category =json.loads(get_categories())
      return { 'category' : category }

