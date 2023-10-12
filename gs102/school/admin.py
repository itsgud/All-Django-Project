from django.contrib import admin
from .models import Student,Teacher,Contractor
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','age','fees']

@admin.register(Teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date','salary']

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display=['id','name','age','date','payment']
   
