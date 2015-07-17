from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)

class Rating(models.Model):
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie)
    
    def __int__(self):
        return self.rating

class Projection(models.Model):
    projection_type = models.CharField(max_length=10)
    when = models.DateTimeField()
    movie = models.ForeignKey(Movie)
    

    def __str__(self):
        return "{} for {} at {}".format(self.projection_type, self.movie.name, self.when)











