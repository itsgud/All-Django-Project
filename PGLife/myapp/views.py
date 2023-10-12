from django.shortcuts import render,HttpResponseRedirect
from .models import City,Banner,Lodge
from django.contrib import messages
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group,User
# Create your views here.
def home(request):
    
    return render(request,'myapp/home.html')

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')

def service(request):
    city=City.objects.all()
    return render(request,'myapp/service.html',{'city':city})

def lodge(request):
    lodge=Lodge.objects.all()
    return render(request,'myapp/lodge.html',{'lodge':lodge})

def banner(request):
    bnr=Banner.objects.all()
    pass



#Signup
def user_signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations !!! You have become an author')
            user=form.save()
    else:
        form=SignUpForm()
    return render(request,'myapp/signup.html',{'form':form})


#Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        
        user=request.user
        curr_id=user.id 
        curr_name=user.username
        print('id of the user is:  ',curr_id)
        print('name is:  ',curr_name)

        full_name=user.get_full_name()
        
        print('name of user is--- ',full_name)
        return render(request,'myapp/dashboard.html',{'full_name':full_name})
    
    else:
        return HttpResponseRedirect('/login/')
    

#user_logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



#Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                print('user nm in login panel-- ',uname)
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully !!!')
                    return HttpResponseRedirect('/dashboard/')
        else:

            form=LoginForm()
        return render(request,'myapp/login.html',{'form':form})

    else:
        return HttpResponseRedirect('/dashboard/')