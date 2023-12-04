from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('form/', views.submit_form, name= 'submit_form'),
    path('django_form/', views.djangoForm, name= 'django_form'),
    path('student/', views.student, name= 'student'),
    path('password/', views.PasswordValidation, name= 'password'),
    
]
