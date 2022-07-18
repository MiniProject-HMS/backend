from django.contrib import admin

from .models import Login, Movement, Student,Complaints, Workers

admin.site.register(Student)
admin.site.register(Complaints)
admin.site.register(Movement)
admin.site.register(Login)
admin.site.register(Workers)