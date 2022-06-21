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
            status = Users.complaint_reg(complaint_data["admission_no"],complaint_data["room_no"],complaint_data["complaint_desc"])
        except:
            status={'data':"not found"}
    return JsonResponse(status,safe=False)


