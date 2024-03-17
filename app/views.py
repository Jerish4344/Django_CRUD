from django.shortcuts import render, redirect
from django.urls import path
from .models import Datas

# Create your views here.
def home(request):
    mydatas = Datas.objects.all()
    if(mydatas!=''):
        return render(request,"home.html",{'datas':mydatas})
    else:
        return render(request,"home.html")

def addDatas(request):
    if request.method=='POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        contact = request.POST['contact']
        mail = request.POST['mail']

        obj = Datas()
        obj.Name = name
        obj.Age = age
        obj.Address = address
        obj.Contact = contact
        obj.Mail = mail
        obj.save()
        mydatas = Datas.objects.all()
        return redirect('home')
    return render(request,"home.html")

def updateData(request, id):
    mydatas = Datas.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        contact = request.POST['contact']
        mail = request.POST['mail']

        mydatas.Name = name
        mydatas.Age = age
        mydatas.Address = address
        mydatas.Contact = contact
        mydatas.Mail = mail
        mydatas.save()

        return redirect('home')

    return render(request,'update.html', {'data':mydatas})

def deleteData(request, id):
    mydatas = Datas.objects.get(id=id)
    mydatas.delete()

    return redirect('home')