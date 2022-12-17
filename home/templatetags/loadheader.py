from django import template
from category.models import Category, SubCategory, SubSubCategory
from product.models import Cart
from about.models import AboutUS
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests
register = template.Library()
@register.filter(name='getcategory')
@register.filter(name='getsubcategory')
@register.filter(name='getsubsubcategory')

def getcategory(value):
    return Category.objects.all()
def getsubcategory(value):
    
    return SubCategory.objects.all()

def getsubsubcategory(value):
    
    return SubSubCategory.objects.all()

@register.filter(name='getrange')
def getrange(value):
    print(value)
    if len(value)<=1:
        
        # print('retunr')
        return ['0:']
    range1 = f"0:{int(len(value)/2)}"
   
    range2 = f"{int(len(value)/2)}:"
    
    return [range1,range2]


@register.filter(name='getcatrange')
def getcatrange(value):
    print(value)
    if len(value)<=2:
        
        # print('retunr')
        return ['0:1:']
    range1 = f"0:{int(value)}"
   
    range2 = f"{int(len(value))}"
    print(range1,range2)
    return [range1,range2]
@register.filter(name='getCart')

def getCart(request):
    return Cart.objects.all()
# @register.filter(name='getuser')
# def getuser(user):
#     return User.objects.get(id=user)
@register.filter(name='getaboutdata')
def getaboutdata(value):
    return AboutUS.objects.all()