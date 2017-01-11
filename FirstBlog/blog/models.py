from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify


class Menu(models.Model):
	title = models.CharField(max_length=128)
	lunch = models.BooleanField(default=True)
	dinner = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.title

class Food(models.Model):
	category = models.ForeignKey(Menu)
	name = models.CharField(max_length=128, unique=True)
	price = models.IntegerField()
	image = models.FileField(upload_to='uploads/food')
	description = models.CharField(max_length=300)
	vegan = models.BooleanField(default=True)
	vegetarian = models.BooleanField(default=True)
	

	def __unicode__(self):
		return self.name

class Employee(models.Model):
	fname = models.CharField(max_length=128)
	lname = models.CharField(max_length=128)
	title = models.CharField(max_length=128)
	bio = models.CharField(max_length=1280)
	tagline = models.CharField(max_length=128)
	image = models.FileField(upload_to='uploads/employee')

	def __unicode__(self):
		return self.fname


		
# Create your models here.
