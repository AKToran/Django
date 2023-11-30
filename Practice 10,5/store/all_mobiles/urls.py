from django.urls import path
from . import views

urlpatterns = [
   path('', views.home),
   path('samsung/', views.samsung),
   path('nokia/', views.nokia),
   path('xiaomi/', views.xiaomi),
    
]
