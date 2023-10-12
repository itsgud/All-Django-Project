from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm
urlpatterns = [
    #path('', views.home),
    path('',views.ProductView.as_view(),name="home"),

    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name='pluscart'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),

    
    path('buy/', views.buy_now, name='buy-now'),
    
    #path('profile/', views.profile, name='profile'),
    path('profile/', views.ProfileView.as_view() , name='profile'),



    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
    path('mobile/',views.mobile,name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    #path('changepassword/', views.change_password, name='changepassword'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view
         (template_name='app/passwordchange.html',
          form_class=MyPasswordChangeForm, success_url=
          '/passwordchangedone/' ),name='passwordchange'),

    path('passwordchangedone/',auth_views.PasswordChangeView.as_view
         (template_name='app/passwordchangedone.html'), 
         name='passwordchangedone'),

    #path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view 
         (template_name='app/login.html',authentication_form=
          LoginForm ), name='login'),
    
    path('logout/',auth_views.LogoutView.as_view
         (next_page='login'),name='logout'), 
    
    
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

