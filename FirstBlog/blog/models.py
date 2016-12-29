from __future__ import unicode_literals

from django.db import models

class Sections(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name

class Menus(models.Model):
	category = models.ForeignKey(Sections)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

# Create your models here.
