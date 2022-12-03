from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class contact_info(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=100)
    text = models.TextField(max_length=500)