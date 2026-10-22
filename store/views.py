from django.shortcuts import render,get_object_or_404

from .models import Product#we want to show all the element of the Product field
from category.models import Category
# Create your views 
def home(request):
    products=Product.objects.all().filter(is_available=True)
   
    
    context={
        'all_items':products,
        
    }
    return render(request,'home.html',context)#always pass context to show the product


def store(request,category_slug=None):
    categories=None
    products=None
    
    if category_slug !=None:
        #take the Category object
        categories=get_object_or_404(Category,slug=category_slug)
        #take product object if categories obj is there
        products=Product.objects.filter(category=categories,is_available=True)
        product_count=products.count()
    else:
        products=Product.objects.all().filter(is_available=True)
        product_count=products.count()
        
    context={
        'store_items':products,
        'product_count':product_count,
    }
    return render(request,'store/store.html',context)

def product_name(request,category_slug=None,product_slug=None):
    return render(request,'store/product_page.html')
    