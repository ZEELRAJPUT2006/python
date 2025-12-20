from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50,null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    image = models.ImageField(upload_to='image')
