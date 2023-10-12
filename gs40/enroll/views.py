from django.shortcuts import render
from .forms import StudentRegistration



# Create your views here.
def showformdata(request):
    if request.method=='POST':
       fm=StudentRegistration(request.POST)
       if fm.is_valid():
           print('form valodated')
           print('Name ',fm.cleaned_data['name'])
           print('Email is: ',fm.cleaned_data['email'])
           print('password is: ',fm.cleaned_data['password'])


    else:
        fm=StudentRegistration()

    return render(request,'enroll/userregistration.html',{'form':fm})
    