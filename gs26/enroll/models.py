from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuname= models.CharField(max_length=45)
    stuemail=models.EmailField(max_length=70)
    stun=models.CharField(max_length=68)

    def __str__(self):
       return self.stuname



