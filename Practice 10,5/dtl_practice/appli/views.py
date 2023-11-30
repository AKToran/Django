from django.shortcuts import render
# from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("hello")
    data = { 'intro': "this is abidul kabir", 'name':'aktoran', 'age': 23, 'null':'', 'size': 125687561,
            'li' : ['django', 'template', 'language'],
            'courses' : [{ 'id': 1, 'name': 'python', 'mentor': 'jhankar mahbub'},
                        {'id': 2, 'name': 'DSA', 'mentor': 'rahat khan pathan'},
                        {'id': 3, 'name': 'django', 'mentor': 'abdullah al naim'}
                                                     ]}
    return render(request, 'appli/home.html', context= data)
