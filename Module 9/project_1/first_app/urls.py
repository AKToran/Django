from django.urls import path
from . import views

# *main url.py etar khobor jane na. janate hobe

urlpatterns = [
    path('courses/', views.courses),
    path('about/', views.about),
    path('', views.first),
]