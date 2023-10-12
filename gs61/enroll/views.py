from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages



# Create your views here.
# def sign_up(request):
#     if request.method=='POST':
#       fm=UserCreationForm(request.POST)
#       if fm.is_valid():
#          fm.save()
#     else:
#        fm=UserCreationForm()
#     return render(request,'enroll/signup.html',{'form':fm})


def sign_up(request):
    if request.method=='POST':
      fm=SignUpForm(request.POST)
      if fm.is_valid():
         messages.SUCCESS(request,'Account Created Successfully !!!')
         fm.save()

    else:
       fm=SignUpForm()
    return render(request,'enroll/signup.html',{'form':fm})
