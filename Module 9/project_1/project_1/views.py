from django.http import HttpResponse

def home(request): #* request must likte hobe. request niye response pathabo
    return HttpResponse("This is home dd  page.")

def contact(request):
    return HttpResponse("this is contact page")
