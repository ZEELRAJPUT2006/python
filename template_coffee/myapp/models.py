from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class product(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    desc = models.TextField()
    image = models.ImageField(upload_to="p_image")