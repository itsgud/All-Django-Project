from django.shortcuts import render
from .forms import StudentRegistration
from .models import User


# Create your views here.
def showformdata(request):
    if request.method=='POST':
       fm=StudentRegistration(request.POST)
       if fm.is_valid():
           nm=fm.cleaned_data['name']
           em=fm.cleaned_data['email']
           pw=fm.cleaned_data['password']
           print('Form is Validated')
           print('NAME is: ',nm)
           print('Emil is: ',em)
           #insert a data
           #reg=User(name=nm,email=em,password=pw)
           #reg.save()

           #update a data by id
           #reg=User(id=1,name=nm,email=em,password=pw)
           #reg.save()

           #delete any data by id
           reg=User(id=1)
           reg.delete()


           
    else:
           fm=StudentRegistration()
           print('ye to get se aa rha hai')
    return render(request,'enroll/userregistration.html',{'form':fm})
    