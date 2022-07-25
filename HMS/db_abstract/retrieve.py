from distutils.log import Log
from urllib import request
from django.http import HttpResponse, JsonResponse
from ..models import Billinfo, Complaints, Login, Student,Movement
from datetime import datetime

class Users():
    def get_users(): #retrieves all data from student model
        users = Student.objects.all().values()
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
    
    def complaint_reg(adm_no,hostel,room_no,desc): #registering complaint into model
        Complaints.objects.create(admission_no_id=adm_no,hostel=hostel,room_no=room_no,complaint_desc=desc)
        return {'status':'success'}

    def complaint_view(hostel,room_no): #sending complaints list to user
        complaint = Complaints.objects.values().filter(hostel=hostel,room_no = room_no)
        complaint_list=list(complaint)
        complaint_dict=({'data':complaint_list})
        return complaint_dict

    def user_profile(adm_no): #sending data to user profile
        profile=Student.objects.values('name','admission_no','hostel','room_no').filter(admission_no=adm_no)
        profile_list=list(profile)
        profile_dict=({'data':profile_list})
        return profile_dict    

    def complaint_work(): #retrieving complaint data
        complaints_work=Complaints.objects.all().values('complaint_id','room_no','complaint_desc','status')
        complaint_list=list(complaints_work)
        complaint_dict=({'data':complaint_list})
        return complaint_dict

    def movement_out(adm_no,hostel): #scanning the QR to go out from the hostel
        current_date=datetime.now()
        Movement.objects.create(admission_no_id=adm_no,hostel=hostel,out_time=current_date)
        id=Movement.objects.values('id').filter(admission_no=adm_no,mess_cut=0)
        id_list=list(id)
        id_dict=({'id':id_list})
        return id_dict 

    def movement_in(id,adm_no): #scanning the QR to enter the hostel
        Movement.objects.filter(id=id).update(in_time=datetime.now())
        in_time=datetime.now()
        out=Movement.objects.filter(id=id)
        for i in out:
            out_t=i.out_time
        cut=(in_time-out_t).days
        if in_time.date().month == out_t.date().month :
            mess=Movement.objects.filter(admission_no=adm_no).values('mess_cut').last()
            mess_cut=mess.get('mess_cut')
        else:
            mess_cut=0
        cut=cut+mess_cut
        if cut >= 15:
            cut=15
        if cut < 5:
            Movement.objects.filter(id=id).update(mess_cut=0)
        elif cut >5 & cut <=15:
            Movement.objects.filter(id=id).update(mess_cut=cut)
        else:
            Movement.objects.filter(id=id).update(mess_cut=15)
        return {"status":"success"}

    def completed_work(id,status):#updating status of the completed work
        Complaints.objects.filter(complaint_id=id).update(status=status)
        return {"status":"success"} 

    def bill_receipt(adm_no,month):#retrieving data for bill information
        bill=Billinfo.objects.values().filter(admission_no=adm_no,month=month)
        bill_list=list(bill)
        bill_dict=({"bill":bill_list})
        return bill_dict


