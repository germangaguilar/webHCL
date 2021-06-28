from django.db import models

from django.contrib.auth.models import User





# Create your models here.
"""
class fecha(models.Model):
    initial_date = models.DateField(required=True)
    exit_date = models.DateField(required=True)
    adults = models.IntegerField(maximum=10)
    kids = models.IntegerField(null=True)
"""
#usuarios
#extraído de curso django
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    picture = models.ImageField(upload_to='profile_pics', blank = 'True')
    def __str__(self):
        return self.user.username


# estos son los de la plantilla de ejemplo (!)
class rooms(models.Model):
    Roomtypecode=models.CharField(max_length=100)
    Roomcode=models.IntegerField()
    typename=models.TextField(max_length=100)
    capacity=models.TextField(max_length=100)
    img=models.ImageField( upload_to = 'pics')
    Availible=models.BooleanField(default=True)

    def __int__(self):
        return self.Roomcode


class usuario(models.Model):
    Nombre=models.CharField(max_length=100, help_text="Introduzca su nombre aquí")
    Apellidos=models.CharField(max_length=100)
    No_of_adults=models.IntegerField()
    no_of_children=models.IntegerField()
    Identity_no=models.CharField(max_length=100)
    Room_code=models.IntegerField()
    No_of_nights=models.IntegerField()
    def __str__(self):
        return self.Nombre
