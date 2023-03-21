from django.db import models

# Create your models here.
from django.db import models
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
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='media/', null='True')
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.category_name
    def save(self, *args, **kwargs):
        if self.id is None or self.slug is None or len(self.slug)==0:
            self.slug = unique_slug_generator(Category,self.category_name)
        super().save()
class SubCategory(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategory",default=1)

    subcategory_name = models.CharField(max_length=100)     
    image = models.ImageField(upload_to ='media/', null='True') 
    slug = models.SlugField(blank=True) 
    class Meta:
        unique_together = ('category_name', 'subcategory_name',)
    def __str__(self) -> str:
        return f"{self.subcategory_name} ({self.category_name})"
    def save(self, *args, **kwargs):
        if self.id is None or self.slug is None or len(self.slug)==0:
            self.slug = unique_slug_generator(SubCategory,self.subcategory_name)
        super().save()
class SubSubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="cat",default=1)
    subcat = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name = 'subcategory')
    name = models.CharField(max_length=100,default='None')     
    
    slug = models.SlugField(blank=True) 
    class Meta:
        unique_together = ( 'subcat', 'name')
    def __str__(self) -> str:
        return f"{self.name} ({self.subcat})"
    def save(self, *args, **kwargs):
        if self.id is None or self.slug is None or len(self.slug)==0:
            self.slug = unique_slug_generator(SubSubCategory,self.name)
        super().save()
class Brands(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='media/', null='True')
    def __str__(self):
        return self.name