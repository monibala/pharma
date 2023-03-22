import uuid
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from category.models import Category, SubCategory
from order.models import OrderItem, update_order
from product.forms import  MyPasswordChangeForm
from product.models import Cart, Product, reviews
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from product.models import Customer_info
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.core.paginator import Paginator
from django.contrib import messages as sms
# Create your views here.
def productsingle(request,slug):
    # if request.user.is_authenticated:
        prod = Product.objects.get(slug=slug)
        rev = reviews.objects.filter(product_name__startswith=prod.product_name)
        cat_prod = Product.objects.filter(category_name=prod.category_name)
        res ={'prod':prod, 'cat_prod':cat_prod, 'rev':rev}
    # else:
        # messages.info(request,'Please Login')
        # return redirect('login')
        return render(request, 'productsingle.html', res)
def review(request):
    prod = Product.objects.all()
    
    if request.method=="POST":
        prod = Product.objects.all()
        rev = reviews()
        rev.name = request.user
        rev.product_name = request.POST['product_name']
        # print(rev.product_name)
        rev.mobile = request.POST['mobile']
        rev.email = request.POST['email']
        rev.comment = request.POST['comment']
        rev.description = request.POST['description']
        rev.rating = request.POST['rating']
        # reviews(name=name,mobile=mobile,email=email,comment=comment,description=description,rating=rating)
        
        # rev.product_name.add('Herbal Juice')
        rev.save()
    # print(prod)
    return render(request, 'review.html',{'prod':prod})
def products(request):
    cat = Category.objects.all()
    subcat = SubCategory.objects.all()
    data = Product.objects.all()
    # Pagination
    p = Paginator(data, per_page=10)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except page_number < 1:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except page_number==0:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    res = {'data':data, 'cat':cat, 'subcat':subcat, 'page_obj': page_obj}
    return render(request, 'products.html', res)
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
    if request.user.is_authenticated:
        user = request.user
        cart_item = Cart.objects.filter(user=user)
        # upt = update_order(user=user)
        if request.method=="POST":
            user = request.user
            name=request.POST['name']
            # lname=request.POST.get('lname')
            email=request.POST['email']
            mobile=request.POST['mobile']
            address=request.POST.get('address')
            state = request.POST.get('state')
            # zipcode = request.POST.get('zipcode')
            city = request.POST.get('city')
            upt = update_order(user = user, name=name,email=email,mobile=mobile,address=address,state=state,city=city)
            # print(check)
            upt.save()
            # upt = update_order(user=user,name=name,email=email,mobile=mobile,address=address,city=city,state=state)
            # upt.save()
        customer = Customer_info.objects.filter(user=user)
        # customer_name = Customer_info.objects.get(user=user)
        print(customer)
        # print(customer_name)
        cart_item = Cart.objects.filter(user=user)
        amount = 0.0
        totalamount=0.0
        shipping_amount = 100.0
        cart_product = [ p for p in Cart.objects.all() if p.user == user]
            
        if cart_product:
            for p in cart_product:
                cost = (p.quantity * p.product.mrp)
                amount += cost
                # order = OrderItem(user=user,name=customer.name,email=customer_name.email,mobile=customer_name.mobile,address=customer_name.apartmentname,city=customer_name.city,state=customer_name.state,order_id=uuid.uuid4(),product=p.product,quntity=p.quantity)        
                order = OrderItem(user=user,order_id=uuid.uuid4(),product=p.product,quntity=p.quantity,code=p.code,size=p.size,color=p.color)
                order.save()
            totalamount = amount + shipping_amount
            # order = OrderItem(user=user,name=customer_name.name,email=customer_name.email,mobile=customer_name.mobile,address=customer_name.apartmentname,city=customer_name.city,state=customer_name.state,amount=totalamount,order_id=uuid.uuid4(),product=p.product,quntity=p.quantity)        
            # order.save()
            order.amount=totalamount   
            # upt = update_order(user=user,name=name,email=email,mobile=mobile,address=address,city=city,state=state)
            # upt.save()
            # upt.product.add(order)
            # To clear cart
        Cart.objects.filter(user=request.user).delete()
        # messages.success(request, 'Your order placed')
        res = {'customer':customer,'amount':amount,'totalamount':totalamount, 'cart_item':cart_item}
        print(amount)
        return render(request, 'checkout.html',res )
        # return render(request, 'checkout.html')
    else:
        messages.warning(request,'Please Login Or Register.')
        return redirect('login_user')
    
@login_required
def show_cart(request):
    if request.user.is_authenticated:

        user= request.user
        carts = Cart.objects.filter(user=user)

        amount= 0.0
        shipping_amount = 100.0
        total_amount = 0.0 
        cart_product = [ p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.offer_price)
                amount += tempamount
                totalamount = amount + shipping_amount


        
            return render(request,'cart.html',{'carts':carts ,'amount':amount ,'totalamount':totalamount })   

        else:
            messages.info(request,f'No item in cart')
            return render(request,'empty.html') 
    # else:
    #     return redirect('login')   
    return render(request, 'cart.html')
# def empty(request):
#     return render(request,'empty.html')
# @login_required
def cart(request):
    if request.user.is_authenticated:
        
        cart_id = request.session.get('cart_id')
        print(cart_id)
    
        quantity = 1
        user = request.user
        product_id = request.GET.get('prod_id')
        prod = Product.objects.get(id = product_id)
    
        item_already_in_cart = Cart.objects.filter(Q(product=prod.id)& Q(user=request.user)).exists()
        if item_already_in_cart:
            return redirect('show_cart')
        else:
            Cart(user=user,product=prod,quantity=quantity,code=prod.code,color=prod.color,size=prod.size).save()
           
        return redirect('show_cart')
    else:
        messages.warning(request,'Please Login Or Register.')
        return redirect('login')  
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
    # if request.method == 'POST':
    #     user=request.user
    #     old_password = request.POST['old_password']
    #     new_password = request.POST['new_password']
    #     confirm_password = request.POST['confirm_password']
    #     if new_password==confirm_password:
    #         password = make_password(new_password, salt=None, hasher='default')
    #         user.password=password
    #     else:
    #         messages.warning("Passwords are not same")
    # return render(request, 'changepassword.html')
   
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('Your password was successfully updated!'))
            return redirect('login')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {
        'form': form
    })
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
            mobile = request.POST['mobile']
            email = request.POST['email']
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
                if len(mobile)>0:
                    
                    ob.mobile=mobile
                if len(email)>0:
                    
                    ob.email=email
               
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
from geopy.geocoders import Nominatim
def checkpincode(request):
    # Importing required module

    zipcode = request.POST.get('zipcode')
    # Using Nominatim Api
    geolocator = Nominatim(user_agent="geoapiExercises")
    # if request.method=="POST":
        # Zipcode input
    # zipcode = request.POST['zipcode']
    print(zipcode)
    # Using geocode()
    location = geolocator.geocode(zipcode)

    # Displaying address details
    print("Zipcode:",zipcode)
    print("Details of the Zipcode:")
    print(location)
    sms.success(request,'Delivery Available')
    return redirect(request.META['HTTP_REFERER'])
    # import requests

    # url = "https://india-pincode-with-latitude-and-longitude.p.rapidapi.com/api/v1/pincode/600001"

    # headers = {
    #     "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
    #     "X-RapidAPI-Host": "india-pincode-with-latitude-and-longitude.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers)

    # print(response.text)
    # return redirect('checkout')
def empty(request):
     Cart.objects.filter(user=request.user).delete()
     
     return render(request,'empty.html')
def pay(request):
    ord = OrderItem.objects.all()
    return render(request,'pay.html',{'ord':ord})