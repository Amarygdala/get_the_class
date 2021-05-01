from django.shortcuts import render
from django.http import Http404 #to call 404
import pyrebase
config = {
    "apiKey": "AIzaSyBNFiTW8_2AeQNQSxlEqBu1qrRKC5S-PKU",
    "authDomain": "dict-131c6.firebaseapp.com",
    "databaseURL": "https://dict-131c6-default-rtdb.firebaseio.com/",
    "projectId": "dict-131c6",
    "storageBucket": "dict-131c6.appspot.com",
    "messagingSenderId": "263354360121",
    "appId": "1:263354360121:web:f71760956a3f3c8f2888e8"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def home(request):
    name = database.child('Data').child('Name').get().val()
    id = database.child('Data').child('ID').get().val()
    project = database.child('Data').child('Project').get().val()
    return render(request, "./DiC/index.html",
                  {"name": name, "id": id, "project": project})
