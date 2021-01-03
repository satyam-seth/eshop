from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_valid=RegexValidator(regex='^\d{10}$')
    phone=models.CharField(validators=[phone_valid],max_length=10)
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.user.username