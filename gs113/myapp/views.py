from django.shortcuts import render
from .models import Song,Page,Post,User
# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def show_user_data(request):
    data1=User.objects.all()
    data2=User.objects.filter(email='contact@geeks.com')
    data3=User.objects.filter(page_page_cat='programming')
    data4=User.objects.filter(post_post_publish_date='2020-05-28')
    data5=User.objects.filter(song_song_duration=3)
    return render(request,'myapp/user.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5})

def show_page_data(request):
    data1=User.objects.all()