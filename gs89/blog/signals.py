from django.contrib.auth.signals import user_logged_in,user_login_failed,user_logged_out
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(user_logged_in,sender=receiver)
def login_success(sender,request,user,**kwargs):
    print('-------------------------')
    print('logged-in Signal... Run Intro..')
    print('Sender:---  ',sender)
    print('Reciever:--- ',request)
    print('User:---  ',user)
    print(f'kwargs: {kwargs}')

#user_logged_in.connect(login_success,sender=User)



@receiver(user_logged_out,sender=User)
def login_success(sender,request,user,**kwargs):
    print('-------------------------')
    print('logged-out Signal... Run outro..')
    print('Sender:---  ',sender)
    print('Reciever:--- ',request)
    print('User:---  ',user)
    print(f'kwargs: {kwargs}')

#user_logged_out.connect(login_out,sender=User)


@receiver(user_login_failed)
def login_failed(sender,credentials ,request,**kwargs):
    print('-------------------------')
    print('logged Failed Signal.....')
    print('Sender:---  ',sender)
    print('Credentials:---  ',credentials)
    print('Reciever:--- ',request)
    
    print(f'kwargs: {kwargs}')

#user_logged_out.connect(login_out,sender=User)



