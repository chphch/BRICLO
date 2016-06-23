from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
import datetime
from time import strftime

SIZE_CHOICES = (
	('S','S'),
	('M','M'),
	('L','L'),
	('XL','XL'),
	('XXL','XXL'),
	('XXXL','XXXL'),
	)

class Start(models.Model):
	style_1_1 = models.CharField(max_length=20, null=True, blank=True)
	style_1_2 = models.CharField(max_length=20, null=True, blank=True)
	style_1_3 = models.CharField(max_length=20, null=True, blank=True)
	style_2 = models.CharField(max_length=20, null=True, blank=True)
	style_3 = models.CharField(max_length=40, null=True, blank=True)
	style_4 = models.CharField(max_length=10, null=True, blank=True)
	style_5 = models.CharField(max_length=100, null=True, blank=True)
	style_6 = models.CharField(max_length=60, null=True, blank=True)
	style_7 = models.CharField(max_length=20, null=True, blank=True)
	style_8 = models.CharField(max_length=40, null=True, blank=True)
	style_9 = models.CharField(max_length=10, null=True, blank=True)
	style_10 = models.CharField(max_length=100, null=True, blank=True)
	style_11 = models.CharField(max_length=100, null=True, blank=True)
	height = models.CharField(max_length=10)
	weight = models.CharField(max_length=10)
	curriculum = models.CharField(max_length=20)
	size_top = models.CharField(max_length=6, choices=SIZE_CHOICES, default='M')
	size_bottom = models.CharField(max_length=6, choices = SIZE_CHOICES, default = 'M')
	kakao = models.CharField(max_length=100)
	address = models.TextField()
	created_date = models.DateTimeField(default=datetime.datetime.now())
	expiration_date = models.DateTimeField(default=datetime.datetime.now().replace(tzinfo=None)+timedelta(days=30))
	user = models.ForeignKey(User, related_name='start',null=True)
	name = models.CharField(max_length=40, null=True)

	def __str__(self):
		expiration_date = str(self.expiration_date.replace(tzinfo=None).strftime("20%y.%m.%d."))
		return expiration_date

