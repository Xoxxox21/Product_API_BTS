from django.shortcuts import render, redirect
import json

# Create your views here.
def index(request):
    file_json = open("static/pizza.json")
    data = json.loads(file_json.read())
    data = data["menu"]
    kategori = []
    context = {
        'data': data
    }
    return render(request, "home.html", context)

def categori(request, kategori):
    file_json = open("static/pizza.json")
    data = json.loads(file_json.read())
    data = data["menu"]
    for i in data:
        if kategori == i['kategori']:
            data = i
    print(data)
    return render(request,"index", data)