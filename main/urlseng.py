from django.contrib import admin
from django.urls import include, path
from .  import views


urlpatterns = [
     path('index/',views.index,name='index'),

     path('logout/',views.logout_view,name='logout'),
     path("base",views.base,name='base'),
     path('esp',include('main.urls')),
     path("quienes_somos",views.about,name='about'),
     path("contacto",views.contact,name='contact'),
     path("ofertas",views.ofertas,name='ofertas'),
     path("servicios",views.servicios,name='servicios'),
     path("registro",views.register_view,name='registro'),
     path("habitaciones",views.rooms,name='rooms'),
]
