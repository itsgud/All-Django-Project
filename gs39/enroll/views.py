from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    if request.method=='POSt':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Validated')
            print('Name: ',fm.cleaned_data['name'])
            print('Agree: ',fm.cleaned_data['agree'])
            print('Roll:',fm.cleaned_data['agree']) 
            print('price:',fm.cleaned_data['price'])
    else:
        fm=StudentRegistration() 
        print('ye to get se aa rha hai')   
    return render(request,'enroll/userregistration.html',{'form':fm})
