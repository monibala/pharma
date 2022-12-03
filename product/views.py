import uuid
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from order.models import OrderItem, update_order
from product.forms import MyPasswordChangeForm
from product.models import Cart, Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from product.models import Customer_info
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
# Create your views here.
def productsingle(request,name):
    prod = Product.objects.get(product_name=name)
    cat_prod = Product.objects.filter(category_name=prod.category_name)
    res ={'prod':prod, 'cat_prod':cat_prod}
    return render(request, 'productsingle.html', res)
def review(request):
    return render(request, 'review.html')
# def checkout(request):
#     user = request.user
    
#     customer = Customer_info.objects.filter(user=user)
#     cart_item = Cart.objects.filter(user=user)
#     amount = 0.0
#     totalamount =0.0
#     shipping_amount = 0.0
#     if request.method=="POST":
#         neworder = OrderItem()
#         neworder.user = request.user
#         neworder.name=request.POST.get('name')
#         neworder.email = request.POST.get('email')
#         neworder.mobile = request.POST.get('mobile')
#         neworder.address = request.POST.get('address')
#         neworder.city = request.POST.get('city')
#         neworder.zipcode = request.POST.get('zipcode')
#         neworder.payment = request.POST.get('payment')
#         neworder.save()
#     user = request.user
    
#     customer = Customer_info.objects.filter(user=user)
#     cart_item = Cart.objects.filter(user=user)
#     amount = 0.0
#     shipping_amount = 0.0
#     cart_product = [ p for p in Cart.objects.all() if p.user == user]
#     # print(cart_product)
#     if cart_product:
#         for p in cart_product:
#             cost = (p.quantity * p.product.mrp)
#             amount += cost
            
#         totalamount = amount + shipping_amount
#         # for item in cart_item:
#         #     amount = amount+item.product.mrp*item.quantity
#         # neworder.amount=totalamount
#         # neworder.save()
        
#     neworderitems = Cart.objects.filter(user=request.user)
#     for item in neworderitems:
#         update_order.objects.create(user=user,prod_order = neworder)
#     # To clear cart
#     Cart.objects.filter(user=request.user).delete()
#     messages.success(request, 'Your order placed')

            
#     return render(request, 'checkout.html', {'amount':amount,'customer':customer,'totalamount':totalamount, 'cart_item':cart_item})
    
    # return render(request, 'checkout.html', {'amount':amount,'customer':customer,'totalamount':totalamount, 'cart_item':cart_item})
def checkout(request):
    user = request.user
    # cart_item = Cart.objects.filter(user=user)
    # if request.method=="POST":
    #     neworder = OrderItem()
    #     neworder.user = request.user
    #     neworder.name=request.POST['name']
    #     neworder.email = request.POST['email']
    #     neworder.mobile = request.POST['mobile']
    #     neworder.address = request.POST['address']
    #     neworder.city = request.POST['city']
    #     neworder.zipcode = request.POST['zipcode']
    #     neworder.payment = request.POST['payment']
    #     neworder.save()
        
        
    customer = Customer_info.objects.filter(user=user)
    print(customer)
    cart_item = Cart.objects.filter(user=user)
    amount = 0.0
    totalamount=0.0
    shipping_amount = 0.0
    cart_product = [ p for p in Cart.objects.all() if p.user == user]
    # print(cart_product)
    if cart_product:
        for p in cart_product:
            cost = (p.quantity * p.product.mrp)
            amount += cost
        totalamount = amount + shipping_amount
        order = OrderItem(user=user,amount=totalamount,order_id=uuid.uuid4(),product=p.product)        
        order.save()
    # To clear cart
    Cart.objects.filter(user=request.user).delete()
    messages.success(request, 'Your order placed')
    return render(request, 'checkout.html', {'customer':customer,'amount':amount,'totalamount':totalamount, 'cart_item':cart_item})
    return render(request, 'checkout.html')
    

def show_cart(request):
    if request.user.is_authenticated:

        user= request.user
        carts = Cart.objects.filter(user=user)

        amount= 0.0
        shipping_amount = 70.0
        total_amount = 0.0 
        cart_product = [ p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.mrp)
                amount += tempamount
                totalamount = amount + shipping_amount


        
            return render(request,'cart.html',{'carts':carts ,'amount':amount ,'totalamount':totalamount })   

        else:
            messages.info(request,f'No item in cart')
            return render(request,'index.html')    
    return render(request, 'cart.html')
@login_required
def cart(request):
    
    cart_id = request.session.get('cart_id')
    print(cart_id)
    if request.user.is_authenticated:
        quantity = 1
        user = request.user
        product_id = request.GET.get('prod_id')
        prod = Product.objects.get(id = product_id)
    
        item_already_in_cart = Cart.objects.filter(Q(product=prod.id)& Q(user=request.user)).exists()
        if item_already_in_cart:
            return redirect('show_cart')
        else:
            Cart(user=user,product=prod,quantity=quantity).save()
           
        return redirect('show_cart')
    else:
        messages.warning(request,'Please Login Or Register.')
        return redirect('index')  
@login_required
def delete(request):
    prod = request.GET.get('remove')
    crt = Cart.objects.filter(user= request.user , product_id = prod)
    crt.delete()

    return redirect('show_cart') 

@login_required
def update(request):
    prod = request.GET.get('min')
    prod1 = request.GET.get('max')
    user = request.user
   
    crt = Cart.objects.filter(user=user , product_id = prod)
    crt1 = Cart.objects.filter(user=user , product_id = prod1)
    # print(crt , crt1)
    if prod!=None:
        # print(prod,'//')
        if len(crt)>0:
            ob=crt[0]
            ob.quantity-=1
            ob.save()
           


    elif prod1!=None:
        if len(crt1)>0:
            ob=crt1[0]
            ob.quantity+=1
            ob.save()
           

    else: 
        crts=Cart(user=User.objects.get(id=request.user),product_id=prod,quantity=1)
        crts.save()

    return redirect('show_cart')   
def account(request):
    if request.method=="POST":
        user = request.user
        name = request.POST['name']
        # lname = request.POST('lname')
        mobile = request.POST['mobile']
        email = request.POST['email']
        res = Customer_info(user=user,name=name,mobile=mobile,email=email)
        res.save()
    return render(request, 'account.html')
def changepassword(request):
    if request.method == 'POST':
        user=request.user
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password==confirm_password:
            password = make_password(new_password, salt=None, hasher='default')
            user.password=password
        else:
            messages.warning("Passwords are not same")
    return render(request, 'changepassword.html')
@login_required
def address(request):
    user = request.user
    addr =  Customer_info.objects.filter(user=user)
    edit = request.POST.get('edit')
    # print(edit)
    dl = request.POST.get('delete')
    addr =  Customer_info.objects.filter(user=user)
    if request.method=="POST":
        if dl!=None:    
            obj = Customer_info.objects.filter(id=dl)
            obj.delete()
        elif edit!=None:
            name = request.POST['name']
            apartmentname = request.POST['apartmentname']
            city = request.POST['city']
            state = request.POST['state']
            # zipcode = request.POST['zipcode']
            # country = request.POST['country']
            cust= Customer_info.objects.filter(id = edit)
            # print(cust)
            if len(cust)>0:
                ob=cust[0] 
                print(ob)
                if len(cust)>0:
                    print(name)
                    ob.name=name
                if len(apartmentname)>0:
                    
                    ob.apartmentname=apartmentname
                if len(city)>0:
                    
                    ob.city=city
                if len(state)>0:
                    
                    ob.state=state
               
                ob.save()
                return redirect('address') 
        else:
             
            name=request.POST['name']
            apartmentname = request.POST['apartmentname']
            city = request.POST['city']
            state = request.POST['state']
            zipcode = request.POST['zipcode']
           
            add_data = Customer_info(user=user,name=name,apartmentname=apartmentname,city=city,state=state,zipcode=zipcode)
            add_data.save()
        addr =  Customer_info.objects.filter(user=user)
        return render(request,'address.html',{'addr':addr})
    return render(request,'address.html',{'addr':addr})