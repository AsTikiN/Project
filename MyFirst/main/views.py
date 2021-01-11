from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,'main/index.html')

def photoes_list(request):
	return render(request, 'main/photoes.html')
