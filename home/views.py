import os
from django.shortcuts import render
import pywhatkit as pwk
from home.models import HomeSlider, Prescriptions


from product.models import Cart, Customer_info, Product, reviews
from django.shortcuts import render,redirect,HttpResponse
from category.models import Brands, Category, SubCategory, SubSubCategory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import CustomerRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
# Create your views here.
def index(request):
    res = {}
    cat = Category.objects.all()
    subcat = SubCategory.objects.all()
    subsubcat = SubSubCategory.objects.all()
    slider = HomeSlider.objects.all()
    deals = Product.objects.filter(category_name__category_name='Featured')
    data1 = Product.objects.filter(category_name__category_name='Basket')
    data2 = Product.objects.filter(category_name__category_name = 'Hamper')
    prod = Product.objects.all()
    brand = Brands.objects.all()
    # rev = reviews.objects.all()
    res = {'slider':slider,'cat':cat, 'subcat':subcat, 'subsubcat':subsubcat,  'prod':prod, 'deals':deals, 'brand':brand,'data1':data1, 'data2':data2}
    return render(request, 'index.html', res)


def login_user(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            # messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'Account does not exist plz sign in')
    form = AuthenticationForm()
    return redirect('index')



def logout_view(request):
    Cart.objects.filter(user=request.user).delete()
    logout(request)
    return redirect('index')
from twilio.rest import Client
TWILIO_ACCOUNT_SID = 'AC7f2e383f0e9ba57d9d1890eb8738aef7'
TWILIO_AUTH_TOKEN = 'ac94fa76bfee0c2b7c587a9cae3ecaf3'
def register(request):
    if request.method=="POST":
        username = request.POST['username']
        email =request.POST['email']
        mobile = request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username,email=email,password=password1)
        user.save()
        c = Customer_info(name=username,email=email,mobile=mobile)
        print(c)
        c.save()
        # client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        # message = client.messages.create(
        #     from_='whatsapp:+918056071345',
        #     body='Hi',
        #     to='whatsapp:+{}'.format(mobile)
        # )

        # print(mobile)
        # print(message.sid)
        # account_sid = os.environ['TWILIO_ACCOUNT_SID']
        # auth_token = os.environ['TWILIO_AUTH_TOKEN']
        # client = Client(account_sid, auth_token)

        # message = client.messages.create(
        #                       body='Hello there!',
        #                       from_='whatsapp:+918056071345',
        #                       to='whatsapp:+919940977404'
        #                   )

        # print(message.sid)
    # if request.method == 'POST':
    #     form = CustomerRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # user = form.save()
    #         # login(request, user)
            
    #         messages.success(request, "Registration successful." )
    #         return redirect("index")
    #     messages.error(request, "Unsuccessful registration. Invalid information.")
    # else:
    #     form =CustomerRegistrationForm()
    # else:
    #     form = CustomerRegistrationForm()
    # return render(request, 'index.html', {'form': form, 'title':'register here'})
    return redirect('index')
def policy(request):
    return render(request,'policy.html')
@login_required
def uploadprescription(request):
    if request.method=="POST":
        print(request.POST,request.FILES)
        # data = {'user':request.user}
        # count = 0
        # for data in request.FILES.getlist('files[]'):
        #     count+=1
        #     if count <=3:
        #         data[f'image{count}'] = data
        # presimg = Prescriptions(**data)
        # presimg.save()
        if request.FILES:
            image = request.FILES.get('prescription[]')
            presimg = Prescriptions(image=image,user = request.user)
            presimg.save()
        
        messages.success(request,'Your Prescription uploaded successfully we will get back to you soon')
        return render(request,'uploadprescription.html',{'presimg':presimg})
    return render(request,'uploadprescription.html')

    # return render(request,'uploadprescription.html')
def search(request):
    cat = Category.objects.all()
    subcat = SubCategory.objects.all()
    if request.method == 'GET':
        query = request.GET.get('search')
        print(query)
        if query:
            
            data = Product.objects.filter(product_name__icontains=query)
            print(data)
            return render(request,'products.html',{'data':data, 'cat':cat, 'subcat':subcat})
        else:
            print('No information available!!')
            return redirect('index') 
# def search(request):
#     context={}
#     data =Product.objects.filter(product_name__icontains=request.GET.get('search'))
#     return render(request, "products.html", {'data':data})
def error_404_view(request, exception):
   
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')