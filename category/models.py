from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=100,unique=True)#url
    description=models.TextField(max_length=255,blank=True)
    cat_images=models.ImageField(upload_to='photo/categories',blank=True)
    
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
        
    def get_urls(self):
        #product by categroy is the link name in urls of stor
        return reverse('prdouct_by_categroy',args=[self.slug])
    
    def __str__(self):
        return self.category_name
#it return a string at last 