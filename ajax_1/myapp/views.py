from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def view(request):
    data = request.GET['data']
    return HttpResponse(f"hello {data}")
