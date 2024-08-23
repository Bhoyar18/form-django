from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=90)
    city=models.CharField(max_length=90)
    email=models.EmailField()
    contact=models.IntegerField()

class Login(models.Model):
    name=models.CharField(max_length=90)
    contact=models.IntegerField()   