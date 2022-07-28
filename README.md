<div align="center">
<a href="https://hoppscotch.io">
<img
src="https://static.djangoproject.com/img/logos/django-logo-positive.svg"
alt="HMS"
height="64"
/>
</div>

# Hostel Management System

## Introduction

Hostel Management System (HMS) is an interactive software, which is used to manage many activities that are being done in a hostel such as a student’s IN&OUT records, monthly mess information, daily attendance, notifications, etc. Since the number of educational institutions has been increasing rapidly, the number of hostels also increased. And hence there is a lot of strain on the person who is running the hostel and software’s not usually used in this context. This particular project deals with the problems of managing a hostel and avoids the problems which occur when carried out manually.

## About the Repo

The current repo consists of backend of Hostel Management System.  
 ## **Requirements**

 - asgiref = 3.5.2
 - backports.entry-points-selectable = 1.1.1 
 - certifi =2022.6.15 
 - charset-normalizer = 2.1.0 
 - distlib = 0.3.3 
 - dj-database-url = 0.5.0 
- Django = 4.0.5 
- django-heroku = 0.3.1 
- filelock = 3.4.0 
- gunicorn = 20.1.0 
- heroku = 0.1.4 
- idna = 3.3 
- mysql-connector-python = 8.0.27 
- platformdirs = 2.4.0 
- psycopg2 = 2.9.3 
- python-dateutil = 1.5 
- requests = 2.28.1 
- six = 1.16.0 
- sqlparse = 0.4.2 
- tzdata = 2022.1
 - urllib3 = 1.26.11 
 - virtualenv = 20.10.0 
 - whitenoise = 6.2.0
 - windows-curses = 2.3.0
 
 ## Commands
 $ `python manage.py runserver`
 
## APIs

    /api/login/?<admission_no,password> : authentication of login [GET]
    /api/complaints/?<admission_no,hotel,room_no,complaint_desc> : registration of complaints [POST]
    /api/profile/?<admission_no> : returns the profile from db [GET]
    /api/works/ : returns all complaints with hostel and room no to worker [GET]
    /api/out/?<admission_no,hostel> : register the out movement from hostel to db of a student [POST]
    /api/in/?<id,admission_no> : register the in movement to hostel to db of a student. *id is generated when a student is going out. [POST]
    /api/bill/?<admission_no,month> : returns the mess bill of a student for a certain month. [GET]

## Users
- #### Admin
- #### Students
- #### Workers
**Learn**

 - [Djanngo Documentation](https://docs.djangoproject.com/en/4.0/)
####  **Support**

 [![Chat on Telegram](https://img.shields.io/badge/chat-Telegram-2CA5E0?logo=telegram)](https://bit.ly/HMS-support)

 
