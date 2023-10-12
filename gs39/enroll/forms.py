from django import forms
class StudentRegistration(forms.Form):
    name=forms.CharField(min_length=5)
    price=forms.DecimalField(min_value=5,max_value=40,max_digits=4,decimal_places=1)
    roll=forms.IntegerField(min_value=3,max_value=50)
    agree=forms.BooleanField(label_suffix='', label='I Agree')
    