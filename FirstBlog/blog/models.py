from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify


class Menu(models.Model):
	title = models.CharField(max_length=128)
	lunch = models.BooleanField(default=True)
	dinner = models.BooleanField(default=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)

		#if self.likes < 0:
		# 	self.likes = 0

		super(Menu, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Food(models.Model):
	category = models.ForeignKey(Menu)
	name = models.CharField(max_length=128, unique=True)
	price = models.IntegerField(max_length=30)
	image = models.FileField(upload_to='uploads/')
	description = models.CharField(max_length=300)
	vegan = models.BooleanField(default=True)
	vegetarian = models.BooleanField(default=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)

		#if self.likes < 0:
		# 	self.likes = 0

		super(Food, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name


# Create your models here.
