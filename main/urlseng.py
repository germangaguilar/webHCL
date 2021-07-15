from django.contrib import admin
from django.urls import include, path
from .  import views


urlpatterns = [
     path('index/',views.index,name='index'),
     path('discover/',views.discover,name='discover'),
     path('rooms/',views.engrooms,name='engrooms'),
     path('offers/',views.offers,name='offers'),
     path('',views.index,name='index'),
]
