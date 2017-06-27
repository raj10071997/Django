# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AppDhanraj(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField()

	def __str__(self):
		return self.title + "-"+ self.likes

#  class Meta:
