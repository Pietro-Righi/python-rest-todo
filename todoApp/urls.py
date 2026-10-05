from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path("getAllTodos" , views.getAllTodos , name="getAllTodos"),
    path("getTodos" , views.getTodos , name="getTodos"),
    path("addTodos" , views.addTodos , name="addTodos"),
    path("updateTodos" , views.updateTodos , name="updateTodos"),
    path("freeTodos" , views.freeTodos , name="freeTodos")
]
