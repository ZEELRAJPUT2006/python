from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone  = data.get('phone')
        student.objects.create(name=name,email=email,phone=phone)
        return HttpResponse("registration successfully")
    
def display(request):
    students = student.objects.all()
    return JsonResponse({"students":list(students.values())})

def delete_data(request):
    sid = request.GET['sid']
    st = student.objects.get(pk=sid)
    st.delete()
    return HttpResponse("student deleted")

def edit_data(request):
    sid = request.GET['sid']
    st = student.objects.filter(id=sid)
    return JsonResponse({"students":list(st.values())})

def update_data(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('id')
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        st = student.objects.get(pk=id)
        st.name = name
        st.email = email
        st.phone = phone
        st.save()

        return HttpResponse("record updated")
    
def search(request):
    value = request.GET['value']
    students = student.objects.filter(name__startswith=value)
    return JsonResponse({"students":list(students.values())})