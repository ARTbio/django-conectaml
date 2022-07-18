from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index1, name = "index1"),
    path("2/", views.index2, name = "index2"),
]