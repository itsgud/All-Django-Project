from django import forms

from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        labels={'name':'Entername : ','password':'Enter password : '
                ,'email': 'Enter Email : '}
        widgets={'password':forms.PasswordInput}