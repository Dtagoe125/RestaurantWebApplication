import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FirstBlog.settings')

import django

django.setup()

from blog.models import Category, Page

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	return c 

def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url = url
	p.views = views
	p.save()
	return p

def populate():
	menu_cat = add_cat('Menu')

	add_page(cat=menu_cat, title="Food Menu", url="http://docs.python.org/2/tutorial/")

	add_page(cat=menu_cat, 
		title="Drink Menu", url="http://www.greenteapress.com/thinkpython/")

	add_page(cat=menu_cat, 
		title="Dessert Menu", url="http://www.korokithakis.net/tutorials/python/")

	for c in  Category.objects.all():
		for p in Page.objects.filter(category=c):
			print "- {0} - {1}".format(str(c), str(p))

if __name__=='__main__':

	print "Starting  population script..."
	populate()
