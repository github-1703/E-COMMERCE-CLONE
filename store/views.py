from django.shortcuts import render

from .models import Product#we want to show all the element of the Product field

# Create your views 
def home(request):
    products=Product.objects.all().filter(is_available=True)
   
    
    context={
        'all_items':products,
        
    }
    return render(request,'home.html',context)#always pass context to show the product


def store(request):
    products=Product.objects.all().filter(is_available=True)
    product_count=products.count()
    context={
        'store_items':products,
        'product_count':product_count,
    }
    return render(request,'store/store.html',context)