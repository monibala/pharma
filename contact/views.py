from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail
from contact.models import contact_info
from django.contrib import messages
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method=="POST":

        name = request.POST['name']
        mobile_number = request.POST['mobile_number']
        subject = request.POST['subject']
        email = request.POST['email']
        text = request.POST['text']
        con =contact_info(name=name,mobile_number=mobile_number,subject=subject,email=email,text=text)
        con.save()
        msg1=(f'\n\n\n Name :  {name} \n Email :  {email} \n Subject : {subject} \n  Message :  {text}')
            
        send_mail(subject,msg1,email,[settings.EMAIL_HOST_USER],fail_silently=False)
        messages.success(request,'Your Message Send Successfully.')
    return render(request, 'contact.html')