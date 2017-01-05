from django.http import HttpResponse
from django.shortcuts import render
from models import Food, Menu


def index(request):
	context_dict = {}
	#request.session.set_test_cookie()
	#if request.session.test_cookie_worked():
	#	print ">>>TEST COOKIE WORKED"
	#	request.session.delete_test_cookie()
	menu_list = Menu.objects.order_by('-likes')[:5] #change 'likes' for ID
	context_dict = {'menus': menu_list}
	#context_dict['food items'] = food_list


	visits =  request.session.get('visits')
	context_dict['visits'] = visits 	
	response = render(request, 'index.html', context_dict)
	
	return response

def menu(request, menu_name_slug):
	context_dict = {}
	context_dict['result_list'] = None
	context_dict['query'] = None

	if request.method == 'POST':
		query = request.POST['query'].strip()

		if query:
			result_list = run_query(query)
			context_dict['result_list'] = result_list
			context_dict['query'] = query
	try:
		menu = Menu.objects.get(slug=menu_name_slug)
		food items = Food.objects.filter(menu=menu)

		context_dict['menu'] = menu
		context_dict['food items'] = food

	except Menu.DoesNotExist:
		pass

	return render(request, 'menu.html', context_dict)

def about(request):
	return HttpResponse("About")

# If it is lunch show "Lunch Menu" based on current timezone of clients website
# def menuTime(request):
#	context_dict = {'boldmessage':'tutorials here!'}
#	return render(request, 'index.html', context_dict)
# Create your views here.

def menuPage(request):
	context_dict = {'boldmessage':'Page Shows Menu'}
	return render(request, 'menu.html', context_dict)