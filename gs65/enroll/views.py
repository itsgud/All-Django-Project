from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from .forms import SignUpForm,EditUserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# SignUp
def sign_up(request):
    if request.method=='POST':
      fm=SignUpForm(request.POST)
      if fm.is_valid():
         messages.success(request,'Account Created Successfully !!!')
         fm.save()

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
               
               return HttpResponseRedirect('/profile/')
      else:
       fm=AuthenticationForm()
       print('login data is coming from get request')
      return render(request,'enroll/userlogin.html',{'form':fm})
   else:
      return HttpResponseRedirect('/profile/')



#profile
def user_profile(request):
   if request.user.is_authenticated:
      if request.method=="POST":
         fm=EditUserProfileForm(request.POST,instance=request.user)
         if fm.is_valid():
            messages.success(request,'Profile is Updated !!!')
            fm.save()
      else:
      #fm=UserChangeForm(instance=request.user)
        fm=EditUserProfileForm(instance=request.user)
      return render(request,'enroll/profile.html',{'name':request.user,'form':fm})
   else:
     return HttpResponseRedirect('/login/')
   
      


#Logout
def user_logout(request):
   logout(request)
   return HttpResponseRedirect('/login/')

#Change Password with old Password
def user_change_pass(request):
   if request.user.is_authenticated: 
      if request.method=="POST":
         fm=PasswordChangeForm(user=request.user,data=request.POST)
         if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,'Password Changed successfully')
            return HttpResponseRedirect('/profile/')
      else:
         fm=PasswordChangeForm(user=request.user)
      return render(request,'enroll/changepass.html',{'form':fm})
   else:
      return HttpResponseRedirect('/login/')
   

#Change Password without old Password
# def user_change_pass1(request):
#    if request.user.is_authenticated: 
#       if request.method=="POST":
#          fm=SetPasswordForm(user=request.user,data=request.POST)
#          if fm.is_valid():
#             fm.save()
#             update_session_auth_hash(request,fm.user)
#             messages.success(request,'Password Changed successfully')
#             return HttpResponseRedirect('/profile/')
#       else:
#          fm=SetPasswordForm(user=request.user)
#       return render(request,'enroll/changepass1.html',{'form':fm})
#    else:
#       return HttpResponseRedirect('/login/')
   



