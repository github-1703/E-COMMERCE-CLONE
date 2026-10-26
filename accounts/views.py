from django.shortcuts import render,redirect
from .forms import RegistrationForms
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    #to submit the form 
    if request.method=='POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            phone_number=form.cleaned_data['phone_number']
            password=form.cleaned_data['password']
            username=email.split("@")[0]
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.phone_number=phone_number #since create_user has no phone_number in it
            user.save()
            messages.success(request,"Account Created Successfully")
    else:
    
        form=RegistrationForms()

    
    context={
            'form':form
        }
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email,password=password)
        
        if user is not None:
            #login the user
            auth_login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid login")
            return redirect('login')
    
    return render(request,'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    
    auth_logout(request)#recursion
    messages.success(request, 'You are logged out.')
    return redirect('login')
    # return render(request,'accounts/logout.html`') 