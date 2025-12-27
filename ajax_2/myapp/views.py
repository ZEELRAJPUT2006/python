from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def view(request):
    data = request.GET['data']
    products = product.objects.filter(name__startswith=data)
    return JsonResponse({"products":list(products.values())})