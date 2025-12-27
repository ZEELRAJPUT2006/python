from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=50)

class country(models.Model):
    name = models.CharField(max_length=50)

class state(models.Model):
    Country = models.ForeignKey(country,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class city(models.Model):
    State = models.ForeignKey(state,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)