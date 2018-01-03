from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return  HttpResponse("hello,world!")
    return  render(request,'blog2/index.html',{'cwm2':'chenwangming2','age':228})

