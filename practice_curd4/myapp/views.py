from django.shortcuts import render, redirect
from myapp.models import *

# Create your views here.
def index(request):
    students = student.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        class_room = request.POST['class_room']
        image = request.FILES.get('image')
        student.objects.create(name=name, email=email, age=age, class_room=class_room, image=image)
        return render(request,'index.html',{'students':students})
    return render(request,'index.html',{'students':students})

def delete_data(request):
    id = request.GET['id']
    s = student.objects.get(pk=id)
    s.delete()
    return redirect('index')

def edit_data(request):
    students = student.objects.all()
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        class_room = request.POST['class_room']
        
        s = student.objects.get(pk=id)
        s.name = name
        s.email = email
        s.age = age
        s.class_room = class_room
        if request.FILES:
            s.image = request.FILES.get('image')
        s.save()
        return render(request,'index.html',{'students':students})

    else:
        id = request.GET['id']
        s = student.objects.get(pk=id)
        return render(request,'index.html',{'students':students,'s':s})

