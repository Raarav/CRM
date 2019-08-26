from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from .models import Task, Register


# Create your views here.

########Task#######

def index(request):
    return render(request, 'index.html')

def task(request):
    form=TaskForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        return render(request,'task.html',{'form':form})


def show(request):
    task = Task.objects.all()
    return render(request,"show.html",{'task':task})
def edit(request, id):
    task = Task.objects.get(id=id)
    return render(request,'edit.html', {'task': task})
def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'task': task})
def destroy(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/show")

#####end Task############

########Login##########

def login(request):
    return render(request, 'login.html')

########endLogin###########
#####Registeration#######

def register(request):
    return render(request, 'register.html')

def fillRegisteration(request):
    form=RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        return render(request, 'register.html', {'form': form})



##### endRegisteration ########

######## calender ##########

def calender(request):
    return render(request, 'calender/demos/week-numbers.html')

######### end calender ############


######## calender ##########

def invoice(request):
    return render(request, 'Invoice/MakeInvoice.html')


def fillInvoice(request):
    form=InvoiceModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/showInvoice')
    return render(request, 'Invoice/MakeInvoice.html', {'form': form})


def showinvoice(request):
    task = MakeInvoiceModel.objects.all()
    return render(request,'Invoice/showInvoice.html',{'task':task})
def editinvoice(request, id):
    task = MakeInvoiceModel.objects.get(id=id)
    return render(request,'Invoice/editInvoice.html', {'task': task})
def updateinvoice(request, id):
    task = MakeInvoiceModel.objects.get(id=id)
    form = InvoiceModelForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect("/showInvoice")
    else:
        return render(request, 'Invoice/editInvoice.html', {'task': task})
def destroyinvoice(request, id):
    task = MakeInvoiceModel.objects.get(id=id)
    task.delete()
    return redirect("/showInvoice")


def viewinvoice(request, id):
    task = MakeInvoiceModel.objects.get(id=id)
    price=float(task.Price)
    quantity=float(task.Quality)
    shipingcost=float(task.ShippingCost)
    amount = price*quantity
    cgst = (5/100)*price
    sgst = (9/100)*price
    Tax = cgst + sgst
    UnitPrice = price - Tax
    Total=amount + shipingcost
    return render(request,'Invoice/ViewInvoice.html', {'task': task,'UnitPrice':UnitPrice,'cgst':cgst,'sgst':sgst,'Tax':Tax,'amount':amount,'Total':Total})

'''def division(request, id):
    task=MakeInvoiceModel.objects.get(id=id)
    price = int(task.Price)
    quantity = int(task.Quality)
    div = price / quantity
    return render(request,'Invoice/ViewInvoice.html',{'task':task,'div':div})

def addition(request, id):
    task=MakeInvoiceModel.objects.get(id=id)
    price=int(task.Price)
    shipingcost = int(task.ShippingCost)
    add = price + shipingcost
    return render(request,'Invoice/ViewInvoice.html',{'task':task,'add':add})'''



######### end calender ############