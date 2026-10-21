from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# .# This class handles the logic for creating users. It contains two functions: one for normal users and one for superusers (admins).

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        
        if not username:
            raise ValueError("User must have username")
      
        user = self.model(
                    email = self.normalize_email(email),
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user   
    
    
    def create_superuser(self,first_name,last_name,username,email, password):
        
       user=self.create_user(
                               first_name=first_name,
                               last_name=last_name,
                               username=username,
                               email = self.normalize_email(email),
                               password=password
       )
       
       user.is_admin=True
       user.is_active=True
       user.is_staff=True
       user.is_superadmin=True
       user.save(using=self._db )
       return user
    

class Account(AbstractBaseUser):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=15)
    
    #required
    
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    
    # This tells Django: "Forget usernames. When a user logs in, treat the email field as their primary credential."
    USERNAME_FIELD='email'
    
    #A list of prompts Django will ask for in the terminal when you run the python manage.py createsuperuser
    REQUIRED_FIELDS=['username','first_name','last_name']
    
    #we are using myaccount manager so have to say``
    objects=MyAccountManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True