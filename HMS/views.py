from curses.ascii import FS
import json
from django.views.decorators.csrf import csrf_exempt
from re import T
from django.http import HttpResponse, JsonResponse
from .db_abstract.retrieve import Users

def get_users(request):
    return JsonResponse(Users.get_users(), safe=False)

def get_pass(request):
    return JsonResponse(Users.get_pass(),safe=False)

def user_profile(request):
    return JsonResponse(Users.user_profile(),safe=False)
    
@csrf_exempt
def handle_auth(request):
    if request.method == 'POST':
        try:
            login_data = json.loads(request.body)
            status = Users.handle_auth(login_data["admission_no"], login_data["password"])
        except:
            status = {"status":"failed"}
    return JsonResponse(status,safe=False)

@csrf_exempt
def complaint_reg(request):
    if request.method =='POST':
        try:
            complaint_data=json.loads(request.body)
            status = Users.complaint_reg(complaint_data["admission_no"],complaint_data["hostel"],complaint_data["room_no"],complaint_data["complaint_desc"])
        except Exception as e :
            print(e)
            status={'data':"not found"}
        return JsonResponse(status,safe=False)
    if request.method =='GET':
        try:
            hostel = request.GET.get("hostel")
            room_no = request.GET.get("room_no")
            complaint=Users.complaint_view(hostel,room_no)
            return JsonResponse(complaint,safe=False)
        except:
            status = {'data':"not found"}
            return JsonResponse(status,safe=False)
        
def complaint_work(request):
    return JsonResponse(Users.complaint_work())

@csrf_exempt
def movement_out(request):
    if request.method == 'POST':
        try:
            out_data=json.loads(request.body)
            status=Users.movement_out(out_data["admission_no"],out_data["hostel"])
        except Exception as e:
            print(e)
            status={'data':"not found"}
        return JsonResponse(status,safe=False)

@csrf_exempt
def movement_in(request):
    if request.method == 'POST':
        try:
            in_data=json.loads(request.body)
            status=Users.movement_in(in_data["id"],in_data["admission_no"])
        except Exception as e:
            print(e)
            status={'data':"not found"}
        return JsonResponse(status,safe=False)

