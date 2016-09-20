from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	context = {}
	context['hello'] = 'Hello World!!! I am luotj'
	return render(request, 'hello.html',context)
