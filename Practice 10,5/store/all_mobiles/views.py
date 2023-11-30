from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'all_mobiles/home.html')


def samsung(request):
    return render(request,'all_mobiles/samsung.html')

def nokia(request):
    return render(request,'all_mobiles/nokia.html')


def xiaomi(request):
    return render(request,'all_mobiles/xiaomi.html')