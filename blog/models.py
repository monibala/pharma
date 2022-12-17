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
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/',null=True)
    author = models.CharField(max_length=100, null=True)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        if self.id is None or self.slug is None or len(self.slug)==0:
            self.slug = unique_slug_generator(Blogs,self.title)
        super().save()