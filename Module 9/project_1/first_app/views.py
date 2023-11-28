from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def courses(request):
    return HttpResponse("this is courses page")

def about(request):
    return HttpResponse("this is about page")

def first(request):
    return HttpResponse("this is first app home page")