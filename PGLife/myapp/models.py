from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField( max_length=50)
    img=models.ImageField( upload_to="myapp/images/city")
    date=models.DateTimeField( auto_now_add=True)

class Banner(models.Model):
    banner_title=models.CharField( max_length=50)
    banner_img=models.ImageField( upload_to="myapp/images/banner")
    banner_desc=models.CharField( max_length=100)
    banner_date=models.DateTimeField(  auto_now_add=True)
    
class Lodge(models.Model):
    name=models.CharField( max_length=50)
    desc=models.CharField( max_length=150)
    address=models.CharField( max_length=250)
    mob=models.BigIntegerField()
    fees=models.IntegerField()
    img=models.ImageField( upload_to="myapp/images/lodge", default=None )
