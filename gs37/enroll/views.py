from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect

# Create your views here.
def thankyou(request):
    return render(request,'enroll/success.html')


def showformdata(request):
    
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():     
          print('Form is validated')
          
          name=fm.cleaned_data['name']
          email=request.POST['email']
          print('NAme',name)
          print('Email',email)
          #fm=StudentRegistration()
          #return render(request,'enroll/success.html',{'nm':name})
          return HttpResponseRedirect('/regi/success/')
    else:
        fm=StudentRegistration()
        print('ye get request se aya hh')

    return render(request,'enroll/userregistration.html',{'form':fm})

