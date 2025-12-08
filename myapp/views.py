<<<<<<< HEAD
from django.shortcuts import render,redirect
from myapp.models import emp

# Create your views here.
def index(request):
    return render(request,'index.html')

def register_emp(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    age = request.POST.get('age')
    salary = request.POST.get('salary')
    dept = request.POST.get('dept')

    if not id:
        emp.objects.create(name=name, age=age, salary=salary, dept=dept)
        return render(request,'index.html')
        
    else :
        e = emp.objects.get(pk=id)
        e.name = name
        e.age = age
        e.salary = salary
        e.dept = dept
        e.save()
        return redirect('display')

def display(request):
    emps = emp.objects.all()
    return render(request,'display.html',{'emps':emps})

def delete_emp(request):
    id = request.GET.get("id")
    e = emp.objects.get(pk=id)
    e.delete()
    return redirect("display")
    
def edit_emp(request):
    id = request.GET.get("id")
    e = emp.objects.get(pk=id)
    return render(request,'index.html',{'e':e})
=======
<<<<<<< HEAD
from django.shortcuts import render
=======
from django.shortcuts import render, redirect
>>>>>>> 5f6774e49d9cd9cf0a3fcb75114a3c24b6e24981
from myapp.models import *

# Create your views here.
def index(request):
<<<<<<< HEAD
    return render(request,'index.html')

def register_student(request):
    first_name = request.POST.get('first_name')
    middle_name = request.POST.get('middle_name')
    last_name = request.POST.get('last_name')
    age = request.POST.get('age')
    subject = request.POST.get('subject')
    class_room = request.POST.get('class_room')

    student.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name, age=age, subject=subject, class_room=class_room)
    return render(request, 'index.html',{'success':'data inserted successfully'})
=======
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

>>>>>>> 5f6774e49d9cd9cf0a3fcb75114a3c24b6e24981
>>>>>>> a6120792a626c93a53c70e731eb58ce82265ed62
