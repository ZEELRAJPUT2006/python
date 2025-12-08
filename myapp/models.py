from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=50)
<<<<<<< HEAD
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField()
    subject = models.CharField()
    class_room = models.CharField()
=======
    last_name = models.CharField(max_length=50)
    rollno = models.IntegerField()
    subject = models.CharField(max_length=70)
    marks = models.IntegerField()
>>>>>>> 5f6774e49d9cd9cf0a3fcb75114a3c24b6e24981
