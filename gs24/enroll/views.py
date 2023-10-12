from django.shortcuts import render
from enroll.models import Student

# Create your views here.
def studentinfo(request):
    stud=Student.objects.all()
    sstud=Student.objects.get(pk=1) #pk---> primary key
    return render(request,'enroll/studetails.html',{'stu':stud,'ss':sstud})