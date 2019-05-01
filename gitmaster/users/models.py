from django.db import models


class MyUser(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    bdate = models.DateField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)