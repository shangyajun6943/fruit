from django.shortcuts import render
from django.http import HttpResponse
from django.conf import *
# Create your views here.

def artic_show(request):
    return  render(request,'showcenter/artic.html')

def vedio_show(request):
    return render(request,'showcenter/vedio.html')