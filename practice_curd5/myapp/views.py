from django.shortcuts import render, redirect
from myapp.models import *
# Create your views here.
def index(request):
    stud = student.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        image = request.FILES['image']
        student.objects.create(name=name,email=email,age=age,image=image)
        return render(request,'index.html',{'stud':stud})
    return render(request,'index.html',{'stud':stud})

def delete_data(request):
    id = request.GET['id']
    s = student.objects.get(pk=id)
    s.delete()
    return redirect('index')

def edit_data(request):
    stud = student.objects.all()
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        
        s = student.objects.get(pk=id)
        s.name = name
        s.email = email
        s.age = age
        if request.FILES:
            s.image = request.FILES.get('image')
        s.save()
        return render(request,'index.html',{'stud':stud})
    
    else:
       id = request.GET['id']
       s = student.objects.get(pk=id) 
       return render(request,'index.html',{'stud':stud,'s':s})
