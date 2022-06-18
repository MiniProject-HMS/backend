from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_users,name='get_users'),
    path('login/',views.handle_auth,name='handle_auth')
]