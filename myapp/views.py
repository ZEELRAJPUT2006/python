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
