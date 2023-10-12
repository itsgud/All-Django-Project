from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.
def regi(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Your Account has been Creates !!!')
            messages.info(request,'Now you can login !!!')

            print(messages.get_level(request))
            messages.debug(request,'This is Debug')
            messages.set_level(request,messages.DEBUG)
            messages.debug(request,'This is New Debug')
            print('new debug value is: ',messages.get_level(request))

    else:
        fm=StudentRegistration()

    return render(request,'enroll/userregistration.html',{'form':fm})



