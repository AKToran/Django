from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    info = {'author':'Abid ul ka bir', 'age':11, 'val':'', 'date': datetime.datetime(1999, 3, 6) , 'l' : ['python', 'is', 'best'], 'courses': [
        {'id' : 1, 'name' : 'Django', 'fee': 1000},
        {'id' : 2, 'name' : 'Bootstrap', 'fee': 500},
        {'id' : 3, 'name' : 'Lavarel', 'fee': 3000},
        {'id' : 4, 'name' : 'PHP', 'fee': 2000}
    ]}
    return render(request, 'con_text/home.html', context=info)
    # * return render(request, 'con_text/home.html', info) just info likleo hobe
    # * always need to be a dictionary
    # ? context: when we send data from backend to frontend, we do it via dictionary. Its called context.
