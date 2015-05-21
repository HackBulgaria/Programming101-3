from django.contrib import admin
from .models import Movie, Projection, Rating

admin.site.register(Movie)
admin.site.register(Projection)
admin.site.register(Rating)
