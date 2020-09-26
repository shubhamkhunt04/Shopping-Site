import os
from django import template
from products.views import get_categories
import json
from products.models import Category
register = template.Library()


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

@register.inclusion_tag('nav.html')
def show_categories():
      category =json.loads(get_categories())
      return { 'category' : category }

