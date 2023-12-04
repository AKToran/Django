from django.shortcuts import render
from .forms import contactForm, StudentData
from .forms import passwordValidation

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    if request.method == 'POST':
        # print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request, 'about.html')

def submit_form(request):
    # print(request.POST)
    # if request.method == 'POST':
    #     name = request.POST.get('username')
    #     email = request.POST.get('email')
    #     return render(request, 'form.html', {'name': name, 'email': email})
    # else:
    return render(request, 'form.html')
     

def djangoForm(request):
    #* best practice:
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # !file section
            # file = form.cleaned_data['file'] 
            # #* file tar jonno. forms.py e je name ta disi ta [ ekhane ]
            # #* upload folder e save korte: 
            # if file != None:
            #     with open('./bird_app/upload/' + file.name, 'wb+') as destination:
            #         for chunk in file.chunks():
            #             destination.write(chunk)
            #         #* wb+: write binary, + for read and write operation. chunks er karone file er smaller version niye kaj korbe jodi huge file ashe

            # image = form.cleaned_data['image']
            # if image is not None:
            #     with open('./bird_app/upload/' + image.name, 'wb+') as destination:
            #         for chunk in image.chunks():
            #             destination.write(chunk)

            print(form.cleaned_data)
            
    else:
        form = contactForm() 
        #* form render korar jonno
        #! return render(request, 'django_form.html') shudo eta dile first load e contactForm er form ta render hobe na

    return render(request, 'django_form.html', {'form': form})


def student(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, "student.html", {'form': form})
   
def PasswordValidation(request):
    if request.method == 'POST':
        form = passwordValidation(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = passwordValidation()
    return render(request, "password.html", {'form': form})


