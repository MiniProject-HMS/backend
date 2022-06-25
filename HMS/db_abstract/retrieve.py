from distutils.log import Log
from urllib import request
from django.http import HttpResponse
from ..models import Complaints, Login, Student

class Users():
    def get_users(): #retrieves all data from student model
        users = Student.objects.all().values_list()
        users_list = list(users)
        users_dict = ({'data':users_list})
        return users_dict

    

    def get_pass(): #retrieving username  and password from login model
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
    
    def complaint_reg(adm_no,room_no,desc): #registering complaint into model
        c = Student.objects.get(pk=adm_no)
        c.complaints_set.create(admission_no=adm_no,room_no=room_no,complaint_desc=desc)
        return {'status':'success'}

    def user_profile(): #sending data to user profile
        profile=Student.objects.all().values('name','admission_no','hostel','room_no')
        profile_list=list(profile)
        profile_dict=({'data':profile_list})
        return profile_dict
        

    def complaint_work(): #retrieving complaint data
        complaints_work=Complaints.objects.all().values('complaint_id','room_no','complaint_desc')
        complaint_list=list(complaints_work)
        complaint_dict=({'data':complaint_list})
        return complaint_dict
   
