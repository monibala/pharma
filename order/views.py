import uuid
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from category.models import SubSubCategory
from order.models import OrderItem, update_order, wishitems
from django.contrib.auth.decorators import login_required
from product.models import Cart, Customer_info, Product
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
@login_required
def order(request):
    op = OrderItem.objects.filter(user=request.user)
    return render(request,'order.html',{'op':op})  
    

def orderdetail(request,id):
    data = OrderItem.objects.get(id=id)
    addr = Customer_info.objects.get(user=request.user)
    res = {'data':data,'addr':addr}
   
    return render(request, 'orderdetail.html',res)

@login_required
def show_wishlist(request):
    wish = wishitems.objects.all()
    return render(request,'wishlist.html',{'wish':wish})

# @login_required
def wishlist(request):
    if request.user.is_authenticated:
        
        user = request.user
        product_id = request.GET.get('prod_id')
        prod = Product.objects.get(id = product_id)
        wishitems(user=user,product=prod).save()
        return redirect('show_wishlist')
    else:
        messages.info(request,'Please Login')
        return redirect('login')

@login_required
def paymentdone(request):
    user = request.user
    custid = request.GET.get('custid')
    print(custid)
    customer = Customer_info.objects.get(email=user.email)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderItem(user=user, customer=customer,product=c.product, quantity = c.quantity).save()
        c.delete()

    return redirect('order')

def thankyou(request):
    return render(request, 'thankyou.html')

@login_required
def removewishitems(request,id):
    rem = wishitems.objects.filter(id=id)
    rem.delete()
    return redirect('show_wishlist')
def recent_prod(request):
    if request.user.is_authenticated:
        user = request.user
        res = {}
        res['prod'] = OrderItem.objects.filter(user=user)
        return render(request,'recent_prod.html',res)