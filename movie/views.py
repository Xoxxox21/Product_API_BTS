from django.shortcuts import render, redirect
import json
import requests
from django.contrib import messages

# Create your views here.
def index(request):
    # get_json = json.loads("http://www.omdbapi.com/?apikey=bc25b0ea&s")
    return render(request, "movie.html")

def search(request):
    if request.method == 'POST':
        title = request.POST["title"]        
        get_json = requests.get("http://www.omdbapi.com/?apikey=bc25b0ea&s="+title).json()
        print(get_json["Response"])
        if get_json["Response"] != True:
            data = get_json["Search"]
            context={
                "data": data,
            }
            return render(request,"movie.html", context)
        else:
            messages.info(request, "Judul yang anda cari tidak ada")
            return render(request,"movie.html")
    else:
        return render(request,"movie.html")