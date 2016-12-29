from django.http import HttpResponse
from django.shortcuts import render
from models import Sections, Menus


def index(request):
	context_dict = {'boldmessage':'tutorials here!'}
	return render(request, 'index.html', context_dict)

def about(request):
	return HttpResponse("About")


# Create your views here.
