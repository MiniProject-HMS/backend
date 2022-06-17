from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.get_users,name='get_users'),
    path('',views.get_pass,name='get_pass'),
]