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

class Start(models.Model):
	size_top = models.CharField(max_length=6, choices=SIZE_CHOICES, default='M')
	size_bottom = models.CharField(max_length=6, choices = SIZE_CHOICES, default = 'M')
	kakao = models.CharField(max_length=100)
	address = models.TextField()
	author = models.ForeignKey('auth.User', related_name='+')
	name = models.CharField(max_length=100, default="")
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.author.username