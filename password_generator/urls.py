from django.urls import path
from generator import views

urlpatterns = [
    path('', views.home),
    path('eggs', views.eggs),
]
