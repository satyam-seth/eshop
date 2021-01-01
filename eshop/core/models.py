from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=PhoneNumberField(null=False,blank=False)
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         attrs_needed = ['_phone', '_city']
#         if all(hasattr(instance, attr) for attr in attrs_needed):
#             Profile.objects.create(user=instance,phone=instance._phone,city=instance._city)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()