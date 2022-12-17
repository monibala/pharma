from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from category.models import Category, SubCategory, SubSubCategory
from product.models import Product
# Create your views here.
def category(request,slug):
    res= {}
    res['category'] = Category.objects.filter(slug=slug)
    # res['pagetitle'] = res['category'].category_name
    cat = Category.objects.all()
    subcat = SubCategory.objects.all()
    subsubcat = SubSubCategory.objects.all()
    # category = Category.objects.get(id=id)
    # subsubcat = SubSubCategory.objects.filter(category_name__category_name=category)
    prod = Product.objects.filter(category_name=slug)
    res = {'cat':cat, 'subcat':subcat,'subsubcat':subsubcat,'prod':prod}
    return render(request, 'category.html', res)
def subcategory(request,slug):
    category = Category.objects.all()
    cat = SubCategory.objects.get(slug=slug)
    subcat = SubCategory.objects.all()
    subsubcat = SubSubCategory.objects.all()
    prod = Product.objects.filter(subcategory_name=cat)
    print(prod)
    res= {'prod':prod,'subcat':subcat,'subsubcat':subsubcat, 'category':category}
    return render(request, 'category.html', res)
def subsubcategory(request,slug):
    data = SubSubCategory.objects.get(slug=slug)
    subsubcat = SubSubCategory.objects.all()
    subcat = SubCategory.objects.all()
    prod = Product.objects.filter(subsubcategory_name=data)
    res= {'prod':prod, 'data':data, 'subcat':subcat, 'subsubcat':subsubcat}
    return render(request, 'category.html', res)