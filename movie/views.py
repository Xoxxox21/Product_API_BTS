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
        if get_json["Response"] == True:
            data = get_json["Search"]
            context={
                "data": data,
            }
            return render(request,"movie.html", context)
        elif get_json["Response"] == False:
            messages.info(request, "judul yang dicari tidak ada")
            return redirect('/search')
    else:
        return render(request,"movie.html")