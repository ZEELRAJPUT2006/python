from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *

# Create your views here.
def login_data(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        u = authenticate(username=username,password=password)
        if u is None:
            return render(request,'login.html')
        else:
            login(request,u)
            return redirect('index')
    return render(request,'login.html')

def reg_data(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        u = User.objects.create(first_name=fname,last_name=lname,email=email,username=username)
        u.set_password(password)
        u.save()
    return render(request,'reg.html')

@login_required(login_url='login')
def index(request):
    products = product.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']
        image = request.FILES.get('image')
        product.objects.create(name=name,price=price,qty=qty,image=image)
    return render(request,'index.html',{'products':products})

def logout_data(request):
    logout(request)
    return render(request,'login.html')

def delete_data(request):
    id = request.GET['id']
    p = product.objects.get(pk=id)
    p.delete()
    return redirect('index')

def edit_data(request):
    products = product.objects.all()
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']

        p = product.objects.get(pk=id)
        p.name = name
        p.price = price
        p.qty = qty
        if request.FILES:
            p.image = request.FILES.get('image')
        p.save()
        return render(request,'index.html',{'products':products})

    else:
        id = request.GET['id']
        p = product.objects.get(pk=id)
        return render(request,'index.html',{'products':products,'p':p})
