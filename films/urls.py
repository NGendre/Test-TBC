from django.urls import path

from . import views

urlpatterns = [
    path('bySearch', views.globalMovieSearch, name='bySearch'),
    path('byTitleArray', views.specificMovieFromArray, name='bySearch'),
]