from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
import datetime

SIZE_CHOICES = (
	('S','S'),
	('M','M'),
	('L','L'),
	('XL','XL'),
	('XXL','XXL'),
	('XXXL','XXXL'),
	)

class Start(models.Model):
	style1 = models.BooleanField(default=False)
	style2 = models.BooleanField(default=False)
	style3 = models.BooleanField(default=False)
	style4 = models.BooleanField(default=False)
	size_top = models.CharField(max_length=6, choices=SIZE_CHOICES, default='M')
	size_bottom = models.CharField(max_length=6, choices = SIZE_CHOICES, default = 'M')
	kakao = models.CharField(max_length=100)
	address = models.TextField()
	name = models.CharField(max_length=100, default="")
	created_date = models.DateTimeField(default=datetime.datetime.now())
	expiration_date = models.DateTimeField(default=datetime.datetime.now().replace(tzinfo=None)+timedelta(days=30))
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="start")

	def __str__(self):
		return self.user.username

