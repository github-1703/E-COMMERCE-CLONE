from django import forms
from .models import Account

class RegistrationForms(forms.ModelForm):
    
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        
        'placeholder':'Enter the password',
        'class':'form-control',#this is the bootstrap class
        
    }))
    
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
            
            'placeholder':'Confirms password'
        }))
    
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email']
        
        
        #dkrectly assign the bootstrap field form-control to other form models created from mpdels.py
    def __init__(self,*args, **kwargs):
        super(RegistrationForms,self).__init__(*args,**kwargs)
        
        self.fields['first_name'].widget.attrs['placeholder']='Enter the first name'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
            self.fields['last_name'].widget.attrs['placeholder']='Enter the last name'
            self.fields['email'].widget.attrs['placeholder']='Enter the email'
            self.fields['phone_number'].widget.attrs['placeholder']='Enter the phone number'
            
    #overiding django clean() funciton
    def clean(self):
        #The line cleaned_data = super(RegistrationForms, self).clean() triggers Django's default validation process first, which ensures all fields match their data types (like verifying an EmailField actually contains an email) and returns a dictionary of validated data.
        cleaned_data=super(RegistrationForms,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError(
                "Password didnot match"
            )
        