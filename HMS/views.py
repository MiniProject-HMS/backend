from curses.ascii import FS
import json
from django.views.decorators.csrf import csrf_exempt
from re import T
from django.http import HttpResponse, JsonResponse
from .db_abstract.retrieve import Users

def get_users(request): #getting the details of all students
    return JsonResponse(Users.get_users(), safe=False)

def get_pass(request):
    return JsonResponse(Users.get_pass(),safe=False)

def user_profile(request): #getting the data of students for their profile
    if request.method == 'GET':
        try:
            adm_no = request.GET.get("admission_no")
            return JsonResponse(Users.user_profile(adm_no),safe=False)
        except Exception as e:
            status = {"status":"failed"}
            return JsonResponse(status,safe=False)
    
@csrf_exempt #password verification
def handle_auth(request):
    if request.method == 'POST':
        try:
            login_data = json.loads(request.body)
            status = Users.handle_auth(login_data["admission_no"], login_data["password"])
        except:
            status = {"status":"failed"}
    return JsonResponse(status,safe=False)

@csrf_exempt #registration of complaints
def complaint_reg(request):
    if request.method =='POST':
        try:
            complaint_data=json.loads(request.body)
            status = Users.complaint_reg(complaint_data["admission_no"],complaint_data["hostel"],complaint_data["room_no"],complaint_data["complaint_desc"])
        except Exception as e :
            print(e)
            status={'data':"not found"}
        return JsonResponse(status,safe=False)
    if request.method =='GET': #viewing the registered complaints of each student in their profile
        try:
            hostel = request.GET.get("hostel")
            room_no = request.GET.get("room_no")
            complaint=Users.complaint_view(hostel,room_no)
            return JsonResponse(complaint,safe=False)
        except:
            status = {'data':"not found"}
            return JsonResponse(status,safe=False)
        
@csrf_exempt        
def complaint_work(request):
    if request.method == 'GET': #wrokers viewing all the complaints registered by students
        return JsonResponse(Users.complaint_work())
    if request.method == 'POST':
        try:
            out_work=json.loads(request.body) #updating of the status of works by workers after completion
            status=Users.completed_work(out_work["complaint_id"],out_work["status"])
        except Exception as e:
            status={'data':"not found"}
        return JsonResponse(status,safe=False)


@csrf_exempt
def movement_out(request):
    if request.method == 'POST': #stroing the data when going out from the hostel
        try:
            out_data=json.loads(request.body)
            status=Users.movement_out(out_data["admission_no"],out_data["hostel"])
        except Exception as e:
            print(e)
            status={'data':"not found"}
        return JsonResponse(status,safe=False)

@csrf_exempt
def movement_in(request):
    if request.method == 'POST': #storing the data when entering the hostel
        try:
            in_data=json.loads(request.body)
            status=Users.movement_in(in_data["id"],in_data["admission_no"])
        except Exception as e:
            print(e)
            status={'data':"not found"}
        return JsonResponse(status,safe=False)

def bill_receipt(request):
    if request.method == 'GET': #getting the bill information of each student by month
        try:
            admission_no = request.GET.get("admission_no")
            month = request.GET.get("month")
            bill = Users.bill_receipt(admission_no,month)
            return JsonResponse(bill,safe=False)
        except Exception as e:
            print(e)
            status = {'data':"not found"}
            return JsonResponse(status,safe=False)
