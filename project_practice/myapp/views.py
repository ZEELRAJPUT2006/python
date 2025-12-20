from django.shortcuts import render, redirect
from myapp.models import emp
# Create your views here.
def index(request):
    emps = emp.objects.all()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        emp.objects.create(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
    return render(request,'index.html',{'emps':emps})

def delete_data(request):
    id = request.GET['id']
    e = emp.objects.get(pk=id)
    e.delete()
    return redirect('index')

def edit_name(request):
    emps = emp.objects.all()
    if request.method == 'POST':
        id = request.POST['id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        e = emp.objects.get(pk=id)
        e.first_name = first_name
        e.last_name = last_name
        e.email = email
        e.username = username
        e.save()
        return render(request,'index.html',{'emps':emps})
    else:
        id = request.GET['id']
        e = emp.objects.get(pk=id)
        return render(request,'index.html',{'emps':emps,'e':e})
