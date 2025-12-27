from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_data(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


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

def index_data(request):
    return render(request,'index.html')