from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

SIZE_CHOICES = (
	('S','S'),
	('M','M'),
	('L','L'),
	('XL','XL'),
	('XXL','XXL'),
	('XXXL','XXXL'),
	)
STYLE_CHOICES = (
	('street','Street'),
	('casual','Casual'),
	('both','Both'),
	)

class Start(models.Model):
	size_top = models.CharField(max_length=6, choices=SIZE_CHOICES, default='M')
	size_bottom = models.CharField(max_length=6, choices = SIZE_CHOICES, default = 'M')
	kakao = models.TextField()
	address = models.TextField()
	author = models.ForeignKey('auth.User', related_name='+')
	name = models.ForeignKey('auth.User', to_field='username', related_name='+', default='User.username')
	style = models.CharField(max_length=6, choices = STYLE_CHOICES, default = "street")
	created_date = models.DateTimeField(default=timezone.now)