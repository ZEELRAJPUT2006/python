from django.shortcuts import render,redirect
from myspp.models import *
# Create your views here.
def index(request):
    prod = product.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']
        image = request.FILES.get('image')
        product.objects.create(name=name,price=price,qty=qty,image=image)
    return render(request,'index.html',{'prod':prod})

def delete_data(request):
    id = request.GET['id']
    prod = product.objects.get(pk=id)
    prod.delete()
    return redirect('index')

def edit_data(request):
    prod = product.objects.all()
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
        return render(request,'index.html',{'prod':prod})
   
    else:
        id = request.GET['id']
        p = product.objects.get(pk=id)
        return render(request,'index.html',{'prod':prod,'p':p})