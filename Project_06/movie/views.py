from django.shortcuts import render,redirect
from .models import Movie
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, "movie/index.html",{"movies":movies})
    
def new(request):
    return render(request, "movie/new.html")
    
def read(request,id):
    movie = Movie.objects.get(pk=id)
    return render(request,"movie/read.html",{"movie":movie})
    
def create(request):
    title = request.POST.get("title")
    audience = request.POST.get("audience")
    genre = request.POST.get("genre")
    score = request.POST.get("score")
    poster_url =request.POST.get("poster_url")
    description = request.POST.get("description")
    
    movie = Movie.objects.create(title=title, audience=audience, genre=genre, score=score, poster_url=poster_url, description=description)
    return redirect(f"/movies/{movie.id}/")


    
def update(request, id):
    movie = Movie.objects.get(id=id)
    
    title = request.POST.get("title")
    audience = request.POST.get("audience")
    genre = request.POST.get("genre")
    score = request.POST.get("score")
    poster_url =request.POST.get("poster_url")
    description = request.POST.get("description")
    
    movie.title = title
    movie.audience = audience
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()
    return redirect(f"/movies/{id}")
    
def edit(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, "movie/edit.html",{"movie":movie})

def delete(request,id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    
    return redirect("/movies")