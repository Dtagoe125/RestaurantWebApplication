from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from forms import ContactForm
from models import Food, Menu, Employee


def index(request):
	context_dict = {}
	#request.session.set_test_cookie()
	#if request.session.test_cookie_worked():
	#	print ">>>TEST COOKIE WORKED"
	#	request.session.delete_test_cookie()
	menu_list = Menu.objects.order_by()[:5] #change 'likes' for ID
	context_dict = {'menus': menu_list}
	#context_dict['food items'] = food_list


	#visits =  request.session.get('visits')
	#context_dict['visits'] = visits 	
	response = render(request, 'index.html', context_dict)
	
	return response

def menu(request, menu_id):
	context_dict = {}
	menu = Menu.objects.get(id=menu_id)

	foods = Food.objects.filter(category=menu).order_by('-name')[:5] #change 'likes' for ID
	context_dict['food_items'] = foods

	return render(request, 'menu.html', context_dict)

def about(request):
	context_dict = {}
	employees = Employee.objects.order_by('-lname')[:5] #change 'likes' for ID
	context_dict['employees'] = employees
	response = render(request, 'about.html', context_dict)
	
	return response

# If it is lunch show "Lunch Menu" based on current timezone of clients website
# def menuTime(request):
#	context_dict = {'boldmessage':'tutorials here!'}
#	return render(request, 'index.html', context_dict)
# Create your views here.

def menuPage(request):
	context_dict = {'boldmessage':'Page Shows Menu'}
	return render(request, 'menu.html', context_dict)


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			form.send_message()
			return HttpResponseRedirect('/')
		else:
			print form.errors
	else:
		form = ContactForm()

	return render(request, 'contact.html', {'form':form})