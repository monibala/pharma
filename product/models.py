from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from category.models import Category, SubCategory, SubSubCategory

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category')
    subcategory_name = models.ForeignKey(SubCategory,on_delete=models.CASCADE,default = 1,related_name='subcat')
    subsubcategory_name = models.ForeignKey(SubSubCategory,on_delete=models.CASCADE,default = 1,related_name='subsubcategory')
    description = models.TextField()
    mrp = models.IntegerField(default=1)
    offer_price = models.IntegerField(default=1)
    offer_percentage = models.IntegerField(default=1)
    image = models.ImageField(null='True',upload_to='media/')

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default =1)

    def __str__(self):
        return str(self.id)    

    @property
    def total_cost(self):
        return self.quantity * self.product.mrp        

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)   
STATE_CHOICES = (
    ('Andaman & Nicobar Islands' , 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunchal Pradesh' , 'Arunchal Pradesh'),
    ('Assam' , 'Assam'),
    ('Bihar' , 'Bihar'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Chandigarh' , 'Chandigarh'),
    ('Chattishgarh' , 'Chattishgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman and Diu' , 'Daman and Diu'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('punjab','punjab'),
    ('Tamil Nadu' , 'Tamil Nadu'),
    ('Telangana','Telangana'),
    ('West Bengal','West Bengal')
)
class Customer_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile= models.IntegerField(null=True)
    email = models.EmailField(null=True)
    apartmentname = models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    zipcode= models.IntegerField(default=1)
    state= models.CharField(choices=STATE_CHOICES,max_length=100)

    def __str__(self):
        return str(self.id)
