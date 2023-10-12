from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from .forms import SignUpForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User,Group
# SignUp
def sign_up(request):
    if request.method=='POST':
      fm=SignUpForm(request.POST)
      if fm.is_valid():
         messages.success(request,'Account Created Successfully !!!')
         #fm.save()

         user=fm.save()
         group=Group.objects.get(name='Editor')
         user.groups.add(group)
    else:
       fm=SignUpForm()
    return render(request,'enroll/signup.html',{'form':fm})

# Login view Function
def user_login(request):
   if not request.user.is_authenticated:
         
      if request.method=='POST':
         print('post method validated')
         fm=AuthenticationForm(request=request,data=request.POST)
         if fm.is_valid():
            print('is_valid validate')
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
               print('user exists ')
               messages.success(request,'Logged in successfully')
               login(request,user)
               
               return HttpResponseRedirect('/dashboard/')
      else:
       fm=AuthenticationForm()
       print('login data is coming from get request')
      return render(request,'enroll/userlogin.html',{'form':fm})
   else:
      return HttpResponseRedirect('/dashboard/')



#Dashboard
def user_dashboard(request):
   if request.user.is_authenticated:
      print('user authenticated !!!')
      return render(request,'enroll/dashboard.html',{'name':request.user.username})
   else:
     return HttpResponseRedirect('/login/')
   
      


#Logout
def user_logout(request):
   logout(request)
   return HttpResponseRedirect('/login/')

