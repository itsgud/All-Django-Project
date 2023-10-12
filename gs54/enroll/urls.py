

from django.urls import path,register_converter
from . import views,converters

register_converter(converters.FourDigitYearConverter,'yyyy')

urlpatterns = [
   
    #path('/<int:my_id>/',views.show_details,name="detail"),
    path('session/<yyyy:year>/',views.show_details,name="detail"),
]
