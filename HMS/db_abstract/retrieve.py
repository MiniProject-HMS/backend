from distutils.log import Log
from urllib import request
from django.http import HttpResponse
from ..models import Login, Student

class Users():
    def get_users():
        users = Student.objects.all().values('name','admission_no','hostel','room_no')  # or simply .values() to get all fields
        users_list = list(users) # important: convert the QuerySet to a list object
        users_dict = ({'data':users_list})
        return users_dict

    

    def get_pass():
        login_id=Login.objects.all().values('admission_no','password')
        login_id_list=list(login_id)
        login_id_dict=({'data':login_id_list})
        return login_id_dict



    def handle_auth(adm_no, passw):
        p=Login.objects.values_list('password').filter(admission_no=adm_no)
        if(p[0][0]==passw):
            return {"status":"success"}
        else:
            return {"status":"failed"}
