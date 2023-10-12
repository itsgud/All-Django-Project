from django.shortcuts import render
from .forms import studentRegistration

# Create your views here.
def student(request):
    fm=studentRegistration()
    return render(request,'enroll/userregistration.html',{'form':fm})

