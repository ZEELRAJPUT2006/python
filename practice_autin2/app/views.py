from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_data(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        u = authenticate(username=username,password=password)
        if u is None:
            return render(request,'login.html')
    return render(request,'login.html')

def reg_data(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        u = User.objects.create(first_name=fname,email=email,username=username)
        u.set_password(password)
        u.save()
    return render(request,'reg.html')