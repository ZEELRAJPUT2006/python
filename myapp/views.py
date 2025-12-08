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