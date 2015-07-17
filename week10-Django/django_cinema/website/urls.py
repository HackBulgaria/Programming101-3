from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show_movie/$', views.show_movie),
    url(r'^rate_movie/$', views.rate_movie)
]
