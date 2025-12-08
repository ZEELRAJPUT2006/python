from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField()
    subject = models.CharField()
    class_room = models.CharField()