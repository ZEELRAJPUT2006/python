from django.shortcuts import render, redirect
from myapp.models import *

# Create your views here.
def index(request):
    students = student.objects.all()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        rollno = request.POST['rollno']
        subject = request.POST['subject']
        marks = request.POST['marks']
        student.objects.create(first_name=first_name, last_name=last_name, rollno=rollno, subject=subject, marks=marks)   
        return render(request,'index.html',{'students':students})
    else:
        return render(request,'index.html',{'students':students})


def edit_data(request):
    students = student.objects.all()
    if request.method == 'POST':
        id = request.POST['id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        rollno = request.POST['rollno']
        subject = request.POST['subject']
        marks = request.POST['marks']

        stud = student.objects.get(pk=id)
        stud.first_name = first_name
        stud.last_name = last_name
        stud.rollno = rollno
        stud.subject = subject
        stud.marks = marks
        stud.save()
        return render(request,"index.html",{'students':students})
    
    else:
        id = request.GET['id']
        stud = student.objects.get(pk=id)
        return render(request,"index.html",{'stud':stud,'students':students})
    
def delete_data(request):
    id = request.GET['id']
    stud = student.objects.get(pk=id)
    stud.delete()
    return redirect("index")

