from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'laptops/home.html')

def dell(request):
    return render(request,'laptops/dell.html')


def asus(request):
    return render(request,'laptops/asus.html')