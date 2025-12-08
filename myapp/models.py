from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rollno = models.IntegerField()
    subject = models.CharField(max_length=70)
    marks = models.IntegerField()