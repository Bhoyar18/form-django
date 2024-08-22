from django import forms
from .models import *

# class Registration(forms.Form):
#     fname=forms.CharField(max_length=50,label="First name")
#     lname=forms.CharField(max_length=20,label="Last name")
#     email=forms.EmailField(label="Email")
#     contact=forms.IntegerField(label="Contact")

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'