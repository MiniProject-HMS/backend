from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_users,name='get_users'),
    path('login/',views.get_pass,name='get_pass'),
]