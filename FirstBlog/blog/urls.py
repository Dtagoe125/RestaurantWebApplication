from django.conf.urls import url 
from blog import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^menu/(?P<menu_name_slug>[\w\-]+)/$', views.menu, name='menu'),
	url(r'^about/', views.about, name="about"),
	]