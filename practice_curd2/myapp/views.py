from django.shortcuts import render, redirect
from myapp.models import student

# Create your views here.
def index(request):
    students = student.objects.all()
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        image = request.FILES.get('image')
        student.objects.create(name=name,email=email,image=image)
    return render(request,'index.html',{'students':students})

def delete_date(request):
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
            image = request.FILES.get('image')

            s = student.objects.get(pk=id)
            s.name = name
            s.email = email
            if request.FILES:
                 s.image = request.FILES['image']
            s.save()
            return render(request,'index.html',{'students':students})
     
     else:
          id = request.GET['id']
          s = student.objects.get(pk=id)
          return render(request,'index.html',{'students':students,'s':s})
          

