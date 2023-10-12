from . import views
from django.urls import path,include

urlpatterns = [
    
    path('registration/',views.showformdata),
    path('success/',views.thankyou),
]