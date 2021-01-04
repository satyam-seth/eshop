from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    date=models.DateField()
    description=models.TextField(max_length=500)
    mrp=models.DecimalField(decimal_places=2,max_digits=7)
    selling_price=models.DecimalField(decimal_places=2,max_digits=10)
    location=models.CharField(max_length=50)

    def __str__(self):
        return self.title