from django.db import models
from store.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id= models.CharField(max_length=230,blank=True)
    date_added=models.DateField(auto_now_add=True)
    

class CartItems(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    is_available=models.BooleanField(default=True)
    