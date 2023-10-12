from django import forms
class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    def clean_name(self):
        valname=self.cleaned_data['name']
        if len(valname)<4:
            raise forms.ValidationError('enter more than or equal 4 char')
        return valname
