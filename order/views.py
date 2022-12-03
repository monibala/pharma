import uuid
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from category.models import SubSubCategory
from order.models import OrderItem, update_order, wishitems
from django.contrib.auth.decorators import login_required
from product.models import Cart, Customer_info, Product
from django.contrib.auth.models import User
# Create your views here.
@login_required
def order(request):
    op = OrderItem.objects.filter(user=request.user)
    return render(request,'order.html',{'op':op})  
    

def orderdetail(request,id):
    data = OrderItem.objects.get(id=id)
    addr = Customer_info.objects.get(user=request.user)
    res = {'data':data,'addr':addr}
    print(res)
    return render(request, 'orderdetail.html',res)
def show_wishlist(request):
    wish = wishitems.objects.all()
    return render(request,'wishlist.html',{'wish':wish})
def wishlist(request):
    if request.user.is_authenticated:
        
        user = request.user
        product_id = request.GET.get('prod_id')
        prod = Product.objects.get(id = product_id)
        wishitems(user=user,product=prod).save()
    return redirect('show_wishlist')

@login_required
def paymentdone(request):
    user = request.user
    custid = request.GET.get('custid')
    print(custid)
    customer = Customer_info.objects.get(id = custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderItem(user=user, customer=customer,product=c.product, quantity = c.quantity).save()
        c.delete()

    return redirect('order')

def thankyou(request):
    return render(request, 'thankyou.html')


   