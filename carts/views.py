from django.shortcuts import render,redirect
from store.models import Product
from .models import CartItems,Cart

from django.http import HttpResponse

# Create your views here.

def _cart_id(request):#we are creating a private function for id
    cart= request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart



def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)#get the product
    try:
        #get the session of the cart_id
        cart=Cart.objects.get(cart_id=_cart_id(request))#get the cart using the cart_id present in the sesion 
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id= _cart_id(request)
        )
    
    cart.save()
    
    #we may have many product in the cart so we have to save it too
    try:
        cart_item= CartItems.objects.get(product=product,cart=cart)
        cart_item.quantity+=1
        cart_item.save()
    except CartItems.DoesNotExist:
        cart_item= CartItems.objects.create(
            product=product,
            cart=cart,
            quantity=1,
            
        )
        
        cart_item.save()
    return HttpResponse(cart_item.product)
    return redirect('cart')
    

#we have to take everything in cart page so modify it
def cart(request,total=0,quantity=0,cart_items=None):
    try:
        cart=Cart.objects.get(_cart_id=_cart_id(request))
        cart_items=CartItems.objects.filter(cart=cart,is_active=True)
        for cart in cart_items:
            total+=(cart_items.product.price * cart_items.quantity)
            quantity+=cart.items.quantity
    except Cart.DoesNotExist:
        pass
    
    context={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items
    }
    
    return render (request,'store/cart.html',context)