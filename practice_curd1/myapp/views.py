from django.shortcuts import render, redirect
from myapp.models import *

# Create your views here.
def index(request):
    emps = emp.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        image = request.FILES.get('image')
        emp.objects.create(name=name,email=email,image=image)
    return render(request,'index.html',{'emps':emps})

def delete_data(request):
    id = request.GET['id']
    e = emp.objects.get(pk=id)
    e.delete()
    return redirect('index')

def edit_data(request):
    emps = emp.objects.all()
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        e = emp.objects.get(pk=id)
        e.name = name
        e.email = email
        e.save()
        return render(request,'index.html',{'emps':emps})
    
    else:
        id = request.GET['id']
        e = emp.objects.get(pk=id)
        return render(request,'index.html',{'emps':emps,'e':e})