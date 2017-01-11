from django.conf.urls import url,include
from blog import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	#url(r'^menu/$', views.menu, name='menu'),
	url(r'^about/', views.about, name='about'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^menu/(?P<menu_id>[\w\-]+)/$', views.menu, name='menu'),
	]