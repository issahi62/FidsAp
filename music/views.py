from django.shortcuts import render
from django.http import HttpResponse, get_object_or_404
# Create your views here.

def index(request):
	return HttpResponse("<h1><center>FidsAp store</center></h1>")

def customerView(request): 
	customer  = Customer.objects.get()
	context = { 
		'customer': customer 
				   } 
	return(request, customer.html, context)

def customer_details(request): 
	cust_details  = Customer.get_object_or_404()
	context = { 
		'customer': csut_details
				   } 
	return(request, customer.html, context)
