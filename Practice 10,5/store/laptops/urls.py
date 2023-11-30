from django.urls import path
from . import views

urlpatterns = [
   path('', views.home),
   path('dell/', views.dell),
   path('asus/', views.asus),
   
    
]
