from . import views
from django.urls import path

urlpatterns=[
    path("",views.home,name='home'),
    path("store_page/",views.store,name='stores'),#change your html to for dynamic urls
    
    #for slugs
    path("store_page/<slug:category_slug>/",views.store,name='prdouct_by_categroy'),
    
    #to got to the product. 
    path("store_page/<slug:category_slug>/<slug:product_slug>/",views.product_name,name='product_name'),
    
] 