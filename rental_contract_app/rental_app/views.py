from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rental_app(request):
    return HttpResponse('<h1>Welcome to our Rental contact app</h1>')