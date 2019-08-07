from django.shortcuts import render
from django.http import HttpRespone

# Create your views here.

def item_displays(request):
	return HttpRespone('<h1><center>Care-free moving items</center></h1>')
	pass
	