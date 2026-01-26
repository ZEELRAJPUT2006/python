from django.db import models
from django.contrib.auth.models import User
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
    image = models.ImageField(upload_to="Product")

class Cart(models.Model):
    Product=models.ForeignKey(product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.IntegerField()
    
    def total_price(self):
        return self.qty*self.Product.price
    
