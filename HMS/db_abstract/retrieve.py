from distutils.log import Log
from urllib import request
from django.http import HttpResponse
from ..models import Complaints, Login, Student

class Users():
    def get_users(): #retrieves all data from student model
        users = Student.objects.all() 
        users_list = list(users)
        users_dict = ({'data':users_list})
        return users_dict

    

    def get_pass(): #retrieving data from login model
        login_id=Login.objects.all()
        login_id_list=list(login_id)
        login_id_dict=({'data':login_id_list})
        return login_id_dict



    def handle_auth(adm_no, passw): #authentication of login
        try:
            p=Login.objects.values_list('password').filter(admission_no=adm_no)
            p[0][0]
        except:
            return {"status":"failed"}
        if(p[0][0]==passw):
            return {"status":"success"}
        else:
            return {"status":"failed"}
    
   
