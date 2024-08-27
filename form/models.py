from django.db import models

# Create your models here.

# class Student(models.Model):
#     name=models.CharField(max_length=90)
#     city=models.CharField(max_length=90)
#     email=models.EmailField()
#     contact=models.IntegerField()

# class Login(models.Model):
#     email=models.CharField(max_length=90)
#     contact=models.IntegerField()   


class StudentModel(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField()
    stu_city = models.CharField(max_length=50)
    stu_mobile = models.IntegerField()
    stu_password = models.CharField(max_length=25)

class StudentQuery(models.Model):
    stu_name=models.CharField(max_length=100)
    stu_email=models.EmailField()
    stu_query=models.CharField(max_length=400)