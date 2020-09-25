from django.shortcuts import render, redirect
from .models import Category,Color,Product,Variants,Size,Images,SocialLinks
from mptt.templatetags.mptt_tags import cache_tree_children
import json
from django.template.loader import render_to_string
from django.http import JsonResponse
from mptt.templatetags.mptt_tags import cache_tree_children
import json
from django.shortcuts import get_object_or_404
import string 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def get_categories():
    root=Category.objects._mptt_filter(level=0)
    root_nodes = cache_tree_children(root.get_descendants())
    dicts = []
    for n in root_nodes:
        dicts.append(recursive_node_to_dict(n))
        jsonTree = json.dumps(dicts,indent=4)
    return jsonTree

def recursive_node_to_dict(node):
    obj = {'title': node.title,'id': node.pk, 'level': node.level,'slug':node.slug, 'get_absolute_url':node.get_absolute_url(),'children': []}
    for child in node.get_children().select_related():
        obj['children'].append(recursive_node_to_dict(child))
    return obj

def product_detail(request,id,slug):
    query = request.GET.get('q')
    
    try:
        product = Product.objects.get(pk=id)
    except:
        return redirect('invalid-url')

    category = Category.objects.get(pk=product.category_id)
    category=Category.objects.get(pk=category.id).get_ancestors()
    images = Images.objects.filter(product_id=id)
    social_links=SocialLinks.objects.filter(product_id=id)
    context = {'product': product,'product_category': category,
               'images': images,'sociallinks':social_links,
               }
    if product.variant !="None": # Product have variants
        if request.method == 'POST': #if we select color
            variant_id = request.POST.get('variantid')
            variant = Variants.objects.get(id=variant_id) #selected product by click color radio
            colors = Variants.objects.filter(product_id=id,size_id=variant.size_id )
            sizes = Variants.objects.raw('SELECT * FROM  products_variants  WHERE product_id=%s GROUP BY size_id',[id])
            query += variant.title+' Size:' +str(variant.size) +' Color:' +str(variant.color)
        else:
            variants = Variants.objects.filter(product_id=id)
            colors = Variants.objects.filter(product_id=id,size_id=variants[0].size_id )
            sizes = Variants.objects.raw('SELECT * FROM  products_variants  WHERE product_id=%s GROUP BY size_id',[id])
            variant =Variants.objects.get(id=variants[0].id)
        
        context.update({'sizes': sizes, 'colors': colors,
                        'variant': variant,'query': query
                        })
    return render(request,'product_details.html',context)




def get_node_from_slug(node):
    for rs in Category.objects.all():
        if rs.slug == node:
            return rs

def category(request,slug):
    slug=slug.split('/')
    sitemap=[]
    
    page = request.GET.get('page', 1)

    found=0
    for rs in slug:
        check_cat=Category.objects._mptt_filter(slug=rs)
        if check_cat:
            found+=1

    if found < len(slug):
        return redirect('invalid-url')
        
    for rs in slug:
        sitemap.append(get_node_from_slug(rs))
    
    if len(slug)>1:
        slug=slug[-1]
    else:
        slug=slug[0]
    
    menu_category=get_categories()
    category = Category.objects._mptt_filter(slug=slug)
    sub_categories=''
    product_list=''
    data_sended=''
    if category.get_descendants():
        sub_categories = cache_tree_children(category.get_descendants())
        paginator = Paginator(sub_categories, 15)
        try:
            sub_categories = paginator.page(page)
        except PageNotAnInteger:
            sub_categories = paginator.page(1)
        except EmptyPage:
            sub_categories = paginator.page(paginator.num_pages)

        data_sended='Category'
    else:
        category=category.get()
        for rs in Category.objects.all():
            if rs.title == category:
                category = rs
                break
        product_list=Product.objects.filter(category_id=category.id)
        paginator = Paginator(product_list, 15)
        try:
            product_list = paginator.page(page)
        except PageNotAnInteger:
            product_list = paginator.page(1)
        except EmptyPage:
            product_list = paginator.page(paginator.num_pages)
        data_sended='Products'
    
    context={
        'sitemap':sitemap,
        'datas':data_sended,
        'products':product_list,
        'sub_categories':sub_categories,
    }
    return render(request,"category_details.html",context)