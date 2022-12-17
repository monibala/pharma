from django.db import models
from django.core.exceptions import ValidationError
def only_int(value):
    excep = ["+","-",","]
    for data in excep: value=value.replace(data,'')
    if value.isdigit()==False:
        raise ValidationError('ID contains characters')
# Create your models here.
class AboutUS(models.Model):
    logo = models.ImageField(upload_to = "logo")
    footerlogo = models.ImageField(upload_to = "logo")
    address = models.TextField()
    phone = models.CharField(max_length=15,validators=[only_int])
    email = models.EmailField(max_length=100)
    website = models.CharField(blank=True,max_length=100)
    otherPhone = models.CharField(max_length=1000,help_text="Separate phone number with (,) Ex: +61 3 1234 5678 , +12 3 1234 5678.......",)
