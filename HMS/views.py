from re import T
from django.http import JsonResponse
from .db_abstract.retrieve import Users

def get_users(request):
    return JsonResponse(Users.get_users(), safe=False)
def get_pass(request):
    return JsonResponse(Users.get_pass(),safe=False)