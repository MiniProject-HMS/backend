from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_users,name='get_users'),
    path('login/',views.handle_auth,name='handle_auth'),
    path('complaints/',views.complaint_reg,name='complaint_reg'),
    path('profile/',views.user_profile,name='user_profile'),
    path('works/',views.complaint_work,name='complaint_work'),
    path('out/',views.movement_out,name='movement_out'),
    path('in/',views.movement_in,name='movement_in'),
    path('bill/',views.bill_receipt,name='bill_receipt'),

]