from django.db import models

# Create your models here.
class emp(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    dept = models.CharField(max_length=50)