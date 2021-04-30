from django.shortcuts import render
from django.http import Http404 #to call 404
# Create your views here.
def home(request):#home page
    return render(request, './DiC/home.html',{})