import os
from django import template

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