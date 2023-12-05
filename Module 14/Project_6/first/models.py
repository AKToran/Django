from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20) #* max length is a must in charfield
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.CharField(max_length=20)

    #* show students by name on admin dashboard
    def __str__(self):
        return f"Roll: {self.roll} - {self.name}"
    
#* super user can do admin operations
# * python manage.py createsuperuser

