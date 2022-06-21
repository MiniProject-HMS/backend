from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_users,name='get_users'),
    path('login/',views.handle_auth,name='handle_auth'),
    path('complaints/',views.complaint_reg,name='complaint_reg'),
    path('works/',views.complaint_work,name='complaint_work')

]