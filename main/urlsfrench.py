from django.contrib import admin
from django.urls import include, path
from .  import views


urlpatterns = [
     path('',views.frindex,name='frindex'),
     path('discover/',views.frdiscover,name='frdiscover'),
     path('chambres/',views.frrooms,name='frrooms'),
     path('offers/',views.froffers,name='froffers'),
]
