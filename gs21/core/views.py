from django.shortcuts import render

# Create your views here.
def aboutUS(request):
    return render(request,'about.html')