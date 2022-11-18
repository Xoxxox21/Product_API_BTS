from django.shortcuts import render, redirect
import json

# Create your views here.
def index(request):
    file_json = open("static/pizza.json")
    data = json.loads(file_json.read())
    data = data["menu"]
    context = {
        'data': data
    }
    return render(request, "home.html", context)

def categori(request, kategori):
    file_json = open("static/pizza.json")
    data = json.loads(file_json.read())
    data = data["menu"]
    hasil = []
    for i in data:
        if kategori == i['kategori']:
            hasil.append(i)
    context={
        "data": hasil,
        "aktif": kategori
    }
    return render(request,"home.html", context)