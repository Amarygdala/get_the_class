from django.shortcuts import render
from PyDictionary import PyDictionary

dictionary=PyDictionary()
# Create your views here.
print(dictionary.translate("Range",'es'))

def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')
