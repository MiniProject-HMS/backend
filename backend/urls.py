from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('HMS', include('HMS.urls')),
    path('admin/', admin.site.urls),
    path('login/',include('HMS.urls')),
]