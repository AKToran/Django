from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('all_mobiles/', include('all_mobiles.urls')),
    path('laptops/', include('laptops.urls')),
]
