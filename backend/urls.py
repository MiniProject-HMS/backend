from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('api/hms/', include('HMS.urls')),
    path('admin/', admin.site.urls),
]