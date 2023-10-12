from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    page_name=models.CharField( max_length=50)
    page_cat=models.CharField( max_length=50)
    page_publish_date=models.DateField()

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_title=models.CharField( max_length=50)
    post_cat=models.CharField( max_length=50)
    post_publish_date=models.DateField()


class Song(models.Model):
    user=models.ManyToManyField(User)
    song_name=models.CharField( max_length=50)
    song_duration=models.IntegerField()
    def written_by(self):
        return ",".join([str(p) for p in self.user.all()])
    
   
