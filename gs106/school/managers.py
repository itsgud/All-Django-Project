from django.db import models
from django.db.models.query import QuerySet


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')
    
  
