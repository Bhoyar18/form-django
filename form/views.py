from django.shortcuts import render
from .form import *
from .models import *

# Create your views here.

# def home(request):
#     form=Registration()
#     # return render(request,"home.html",{"form":form})
#     if request.method=="POST":
#         form=Registration(request.POST)
        
#         if form.is_valid():
#             fname=form.cleaned_data["fname"]
#             lname=form.cleaned_data["lname"]
#             email=form.cleaned_data["email"]
#             contact=form.cleaned_data["contact"]
#             print(fname,lname,email,contact)
#             # data={"fname":fname,"lname":lname,"email":email,"contact":contact}
#     return render(request,"home.html",{"form":form})


def home(request):
    form=StudentForm()
    # return render(request,"home.html",{"form":form})
    if request.method=="POST":
        form=StudentForm(request.POST)
        
        if form.is_valid():
            name=form.cleaned_data["name"]
            city=form.cleaned_data["city"]
            email=form.cleaned_data["email"]
            contact=form.cleaned_data["contact"]
            print(name,city,email,contact)
            # data={"fname":fname,"lname":lname,"email":email,"contact":contact}
            # Student.objects.create(Stu_name=name,Stu_city=city,Stu_email=email,Stu_contact=contact)
            form.save()
    return render(request,"home.html",{"form":form})