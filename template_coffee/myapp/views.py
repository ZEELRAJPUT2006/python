from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def contact(request):
    return render(request,'contact.html')

@login_required(login_url='login')
def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
def service(request):
    return render(request,'service.html')

@login_required(login_url='login')
def menu(request):
    products = product.objects.all()
    catgories = category.objects.all()
    return render(request,'menu.html',{'products':products, 'categories':catgories})

@login_required(login_url='login')
def reservation(request):
    return render(request,'reservation.html')

@login_required(login_url='login')
def testimonial(request):
    return render(request,'testimonial.html')

def login_data(request):
  if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        u = authenticate(username=username, password=password)

        if u is None:
            return render(request, "login.html", {'err': 'Invalid username or password'})
        else:
            login(request, u)  
            return redirect('index')

  return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        u = User(first_name=first_name,last_name=last_name,email=email,username=username)
        u.set_password(password)
        u.save()
    return render(request,'registration.html',{'msg':'registration successfully'})

def logout_data(request):
    logout(request)
    return redirect('index')