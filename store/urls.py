from . import views
from django.urls import path

urlpatterns=[
    path("",views.home,name='home'),
    path("store_page/",views.store,name='store')#change your html to for dynamic urls
] 