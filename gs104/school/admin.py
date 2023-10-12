from django.contrib import admin
from .models import ExamCenter,MyExamCenter
# Register your models here.
@admin.register(ExamCenter)
class ExamcenterAdmin(admin.ModelAdmin):
    list_display=['id','cname','city']


@admin.register(MyExamCenter)
class MyExamcenterAdmin(admin.ModelAdmin):
    list_display=['id','cname','city']
