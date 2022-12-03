from django.shortcuts import render
from home.models import Prescriptions

# Create your views here.
from product.models import Product
from django.shortcuts import render,redirect,HttpResponse
from category.models import Brands, Category, SubCategory, SubSubCategory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import CustomerRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    res = {}
    cat = Category.objects.all()
    subcat = SubCategory.objects.all()
    subsubcat = SubSubCategory.objects.all()
    deals = Product.objects.filter(category_name__category_name='Featured')
    prod = Product.objects.all()
    brand = Brands.objects.all()
    res = {'cat':cat, 'subcat':subcat, 'subsubcat':subsubcat,  'prod':prod, 'deals':deals, 'brand':brand}
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
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})
def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
           
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('index')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'index.html', {'form': form, 'title':'register here'})

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
        return render(request,'uploadprescription.html')
    return render(request,'uploadprescription.html')

    # return render(request,'uploadprescription.html')