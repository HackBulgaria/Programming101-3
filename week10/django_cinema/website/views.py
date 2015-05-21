from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import Movie, Rating

def index(request):
    movies = Movie.objects.all()

    return render(request, "index.html", locals())

def show_movie(request):
    movie_id = request.GET.get("movie_id")
    if movie_id is None:
        movie = Movie.objects.first()
    else:
        movie = get_object_or_404(Movie, pk=movie_id)
        ratings = movie.rating_set.all()
        total_ratings = 0
        avg_rating = 0.0

        for rating in ratings:
            total_ratings += int(rating)
        
        if len(ratings) == 0:
            avg_rating = 0
        else:
            avg_rating = total_ratings / len(ratings)
        

    return render(request, "movie.html", locals())

def rate_movie(request):
    if request.method == "POST":
        movie_id = request.POST.get("movie_id")
        rating = request.POST.get("rating")
        
        if movie_id is None or rating is None:
            return HttpResponse("Bad Request")
        
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.rating_set.add(Rating(rating=rating))
        movie.save()

    return redirect("/show_movie?movie_id={}".format(movie_id))











