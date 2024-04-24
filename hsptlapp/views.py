from django.shortcuts import render,redirect
from .models import Doctors
from .forms import BookingForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def doctors(request):
    dict_doc={
        'doc':Doctors.objects.all()
        }
    return render(request,'doctors.html',dict_doc)
def booking(request):
    if request.method == "POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
  
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
def contact(request):
    return render(request,'contact.html')