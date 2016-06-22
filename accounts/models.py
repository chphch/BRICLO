from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.
GENDER_CHOICES = (
    		('MEN' , 'MEN'),
    		('WOMEN' , 'WOMEN'),
    	)
SIZE_CHOICES = (
	('S','S'),
	('M','M'),
	('L','L'),
	('XL','XL'),
	('XXL','XXL'),
	('XXXL','XXXL'),
	)


class Profile(models.Model):
    address = models.CharField(max_length=300)
    gender= models.CharField(max_length=6, choices = GENDER_CHOICES, default='MEN')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=40,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        profile = Profile(user=user)
        profile.save()

post_save.connect(create_profile, sender=User)
