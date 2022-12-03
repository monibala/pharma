from django.db import models

from product.models import Cart, Customer_info, Product
from django.contrib.auth.models import User
# Create your models here.
class wishitems(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
   

    def __str__(self):
        return str(self.id)
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)   
class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='prod')
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True, verbose_name="product_pyment_id")
    name=models.CharField(max_length=50,null=True)
    
    
    
    address=models.TextField(null=True)
    city=models.CharField(max_length=50,null=True)
    
    zipcode=models.IntegerField(default=1)
    mobile=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    quntity=models.IntegerField(default=1)
    payment=models.CharField(max_length=100,null=True)
    amount=models.IntegerField(default=1)
    
    status = models.CharField(max_length=50 , choices=STATUS_CHOICES, default ='Pending')
    order_date=models.DateTimeField(auto_now_add=True,null=True)
    def save(self, *args, **kwargs):
        if self.order_id is None and self.order_date and self.id:
            self.order_id = self.order_date.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.product.product_name[:10]+' '+self.name

class update_order(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    prod_orders=models.ManyToManyField(OrderItem,verbose_name='product_order')
    
    updt_id=models.CharField(unique=True, max_length=1000, null=True, blank=True,  verbose_name="updt_pyment_id")
    updt_date=models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if self.updt_id is None and self.updt_date and self.id:
            self.updt_id = self.updt_date.strftime('PAYMENT%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)