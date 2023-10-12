from django.shortcuts import render

def show_details(request,year):
    st={'id':year}
    return render(request,'enroll/show.html',st)

