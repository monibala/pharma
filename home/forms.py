from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from product.models import Customer_info
class loginform(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(label=('Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
class CustomerRegistrationForm(UserCreationForm):
    email = forms.CharField(label='Email',required=True , widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    mobile = forms.IntegerField(label='mobile',required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}
    