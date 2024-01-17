from django.shortcuts import render
from django.http import HttpResponse
from . models import Departments,Doctors,Booking,Contact
from .forms import BookingForm

# Create your views here.

def index(request):
    return render(request,"index1.html")

def base(request):
    return render(request,"base2.html")

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def booking(request):
    # dict_p={
    #     'pat':Booking.objects.all()
    # }
    form=BookingForm
    dict_form={
        'form':form
    }
    return render(request,"booking.html",dict_form)

def contacts(request):
   if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        print(name,phone,email)
        query = Contact(name=name,phone=phone,email=email)
        query.save()
        return render(request,"contacts.html",)

def departments(request):
    return render(request,"departments.html")

def doctors(request):
    dict_doc={
        'doc':Doctors.objects.all()
    }
    return render(request,"doctors.html",dict_doc)

def departments(request):
    dict_dep={
        'dept':Departments.objects.all()
    }
    return render(request, 'departments.html',dict_dep)
