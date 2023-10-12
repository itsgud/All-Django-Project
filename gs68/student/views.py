from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response = render (request,'student/setcookie.html')
    response.set_cookie('name','sonam',max_age=60)
    return response

def getcookie(request):
     #nm=request.COOKIES['name']
     #nm=request.COOKIES.get('name')
     nm=request.COOKIES.get('name',"Guest")
     return render(request,'student/getcookie.html',{'xyz':nm})



def delcookie(request):
     response= render(request,'student/delcookie.html')
     response.delete_cookie('name')
     return response



