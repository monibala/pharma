from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from category.models import Brands, Category, SubCategory, SubSubCategory
from django.utils.text import slugify
import random, string
# Create your models here.
def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    slug=slugify(new_slug)[:50]
    Klass = instance
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = slugify(str(slug)[:46]+get_random_string(4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
def get_random_string(size):
    return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = size))
color_choice = (
    ('WHITE' ,'WHITE'),
    ('BLUE','BLUE'),
    ('PINK','PINK'),
    ('MAROON','MAROON'),
    ('IVORY','IVORY'),
    ('RED','RED'),
    ('ORANGE','ORANGE'),
    ('GREEN','GREEN'),
    ('YELLOW','YELLOW'),
    ('GOLDEN','GOLDEN'),
    ('BROWN','BROWN'),
    ('SILVER','SILVER'),

)
size_choice = (
    ('LARGE','LARGE'),
    ('MEDIUM','MEDIUM'),
    ('SMALL','SMALL'),
    
)
avail_choice = (
    ('IN STOCK','IN STOCK'),
    ('OUT OF STOCK', 'OUT OF STOCK'),
)
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category')
    subcategory_name = models.ForeignKey(SubCategory,on_delete=models.CASCADE,blank=True,null=True,related_name='subcat')
    subsubcategory_name = models.ForeignKey(SubSubCategory,on_delete=models.CASCADE,blank=True,null=True,related_name='subsubcategory')
    # brands = models.ForeignKey(Brands,on_delete=models.CASCADE,default = 1,related_name='brand')
    description = models.TextField()
    mrp = models.IntegerField(default=1)
    offer_price = models.IntegerField(default=1)
    offer_percentage = models.IntegerField(default=1)
    image = models.ImageField(null='True',upload_to='media/')
    color = models.CharField(max_length=100,choices=color_choice,blank=True,default='WHITE')
    size = models.CharField(max_length=100,choices=size_choice,blank=True,default='SMALL')
    code = models.CharField(max_length=100,default='DBMS1')
    availability = models.CharField(max_length=100,choices=avail_choice,default='IN STOCK')
    slug = models.SlugField(blank=True) 
    def save(self, *args, **kwargs):
        if self.id is None or self.slug is None or len(self.slug)==0:
            self.slug = unique_slug_generator(Product,self.product_name)
        super().save()
    def __str__(self):
        return self.product_name
class Cart(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    code = models.CharField(max_length=100,default='None')
    color = models.CharField(max_length=100,default='None',blank=None)
    size = models.CharField(max_length=100,blank=None,default='None')
    quantity = models.PositiveIntegerField(default =1)

    def __str__(self):
        return str(self.product)    

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
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile= models.IntegerField(null=True)
    email = models.EmailField(null=True)
    apartmentname = models.CharField(max_length=200,blank=True)
    city= models.CharField(max_length=100,blank=True)
    zipcode= models.IntegerField(default=1)
    state= models.CharField(choices=STATE_CHOICES,max_length=100,blank=True)
    
    def __str__(self):
        return str(self.name)
RATING_CHOICES = (
        (5, '*****'),
        (4, '****'),
        (3, '***'),
        (2, '**'),
        (1, '*'),
    )
class reviews(models.Model):
    product_name = models.CharField(max_length=250,null=True)
    name = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    email = models.EmailField(max_length=100)
    mobile = models.IntegerField(null=True)
    comment = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    slug = models.SlugField(blank=True)
    def __str__(self) -> str:
        return str(self.id)
    # image = models.ImageField(upload_to='media', null=True)
    # def __str__(self) -> str:
    #     return f"{self.name} ({self.product_name})"
    def save(self, *args, **kwargs):
        if self.id is None or self.slug is None or len(self.slug)==0:
            self.slug = unique_slug_generator(Product,self.product_name)
        super().save()