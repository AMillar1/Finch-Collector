from django.shortcuts import render
from .models import Finch

# class Finch: 
#     def __init__(self, name, beaklength, age):
#         self.name = name
#         self.beaklength = beaklength
#         self.age = age

# finches = [
#     Finch('Charles', '3cm', '212'),
#     Finch('Percy', '2cm', '151'),
#     Finch('David', '2cm', '111'),
# ]

# Add the following import
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello!</h1>')
def about(request):
    return render(request, 'about.html')
def finches_index(request):
    finches = Finch.objects.all()
    return render(request, "finches/index.html", {'finches' : finches})

