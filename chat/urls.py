from django.contrib import admin
from django.urls import path, include
from chat import views


urlpatterns = [
     path('room/', views.Rooms),
     path('dialog/', views.DialogGet),
     path('dialog-post/', views.DialogPost)
]