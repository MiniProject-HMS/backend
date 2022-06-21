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
def complaint_work(request):
    return JsonResponse(Users.complaint_work())


