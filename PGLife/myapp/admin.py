from django.contrib import admin
from .models import City,Banner,Lodge
# Register your models here.


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=['id','name','img','date']

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display=['id','banner_title','banner_img','banner_desc','banner_date']

@admin.register(Lodge)
class LodgeAdmin(admin.ModelAdmin):
    list_display=['id','name','desc','address','mob','fees','img']
