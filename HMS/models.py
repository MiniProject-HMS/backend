from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    admission_no= models.IntegerField(primary_key=True)
    hostel=models.CharField(max_length=50,default="null")
    room_no=models.IntegerField(default=0)
    password=models.CharField(max_length=16, default="lbscek123")
    def __str__(self):
        return self.name

    
