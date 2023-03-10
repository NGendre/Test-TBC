from django.urls import path

from . import views

urlpatterns = [
    path('/bySearch', views.globalFastAndFuriousSearch, name='bySearch'),
    path('/byTitleArray', views.specificFastAndFuriousSearchFromArray, name='bySearch'),
]