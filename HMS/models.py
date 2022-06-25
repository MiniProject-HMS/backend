from tkinter import CASCADE
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    admission_no= models.IntegerField(primary_key=True)
    hostel=models.CharField(max_length=50,default="null")
    room_no=models.IntegerField(default=0)
    phone_no=models.IntegerField(default=0000000000)
    address=models.CharField(max_length=100,default="null")

class Login(models.Model):
    admission_no=models.ForeignKey(Student,on_delete=models.CASCADE)
    password=models.CharField(max_length=16, default="lbscek123")

class Complaints(models.Model):
    complaint_id=models.BigAutoField(primary_key=True)
    admission_no=models.ForeignKey(Student,on_delete=models.CASCADE)
    hostel=models.CharField(max_length=20,default='null')
    room_no=models.IntegerField()
    complaint_desc=models.TextField()
    status=models.BooleanField(default=False)

class Workers(models.Model):
    name=models.CharField(max_length=25)
    designation=models.CharField(max_length=25)
    phone_no=models.IntegerField(default=0)

    
    
