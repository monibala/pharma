from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Prescriptions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/',blank=True)
    
    def __str__(self):
        return str(self.id)
class HomeSlider(models.Model):
    image = models.ImageField(upload_to='media/',null=True)