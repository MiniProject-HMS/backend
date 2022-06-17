from ..models import Student

class Users():
    def get_users():
        users = Student.objects.all().values('name','admission_no','hostel','room_no')  # or simply .values() to get all fields
        users_list = list(users) # important: convert the QuerySet to a list object
        users_dict = ({'data':users_list})
        return users_dict

    

    def get_pass():
        login_id=Student.objects.all().values('admission_no','password')
        login_id_list=list(login_id)
        login_id_dict=({'data':login_id_list})
        return login_id_dict