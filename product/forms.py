from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import password_validation

from order.models import OrderItem
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=('Old Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','auto-focus':'True','class':'form-control'}))
    new_password1 = forms.CharField(label=('New Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=('Confirm New Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
# class Checkout(forms.ModelForm):
#     class Meta:
#         model = OrderItem
#         fields = ["name","email" ,"mobile","address","city","state", "zipcode"]
        # labels = {'fullname': "Name", "mobile_number": "Mobile Number",}