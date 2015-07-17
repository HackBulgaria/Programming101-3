# Cinema Reservation System with Django

In order to get started with Django, you are going to have the following task:

## Getting Started - first exercise

1. Create a Django project, that will represent our cinema reserveration system.
2. Create a new app, called `website`, where you are going to add write your code.
3. Create models for all of the cinema logic - https://github.com/HackBulgaria/Programming101-3/tree/master/week8/3-Cinema-Reservation-System - Check for how to make foreign keys with Django - https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_one/ and how to make many-to-many - https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_many/ using Django's ORM
4. Create a index view, where you are listing all movies and for each movie, all projections for it. You will have to use Django's templates - https://docs.djangoproject.com/en/1.8/topics/templates/


Here is an example of the structure and the final HTML that want:


```html
<h1>Movies and projections:</h1>

<h2>The Hunger Games: Catching Fire</h2>

<p>Rating of the movie: 7.9</p>

<strong>Projections:</strong>

<ul>
  <li>2014-04-01 at 19:10 - 3D</li>
  <li>2014-04-01 at 19:00 - 2D</li>
  <li>2014-04-02 at 21:00 - 4DX</li>
</ul>

<h2>Wreck-It Raplh</h2>

<p>Rating of the movie: 7.8</p>

<strong>Projections:</strong>

<ul>
  <li>2014-04-02 at 22:00 - 3D</li>
  <li>2014-04-02 at 19:00 - 2D</li>
</ul>

<h2>Her</h2>

<p>Rating of the movie: 8.3</p>

<strong>Projections:</strong>

<ul>
  <li>2014-04-05 at 20:20 - 2D</li>
</ul>

```
