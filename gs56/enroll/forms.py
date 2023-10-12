from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
      model=User
      fields=['stud_name','email','password']


class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields=['teacher_name','email','password']

