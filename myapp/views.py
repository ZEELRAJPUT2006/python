from django.shortcuts import render
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def register_student(request):
    first_name = request.POST.get('first_name')
    middle_name = request.POST.get('middle_name')
    last_name = request.POST.get('last_name')
    age = request.POST.get('age')
    subject = request.POST.get('subject')
    class_room = request.POST.get('class_room')

    student.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name, age=age, subject=subject, class_room=class_room)
    return render(request, 'index.html',{'success':'data inserted successfully'})
