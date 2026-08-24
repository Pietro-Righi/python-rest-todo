from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import TodosSerializer


@api_view(["GET"])
def getAllTodos(request):
    todos = Todos.objects.all()
    serializer = TodosSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getTodos(request):
    todos = Todos.objects.filter(stato=False)
    serializer = TodosSerializer(todos, many=True)
    return Response(serializer.data)



@api_view(["POST"])
def addTodos(request):
    serializer = TodosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def updateTodos(request):
    todo = Todos.objects.get(id=request.data.get("id"))
    serializer = TodosSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# Create your views here.
