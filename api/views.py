from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

# Create your views here.
@api_view(['GET'])
def TaskList(request,format=None):

    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def TaskAdd(request,format=None):
    serializer =  TaskSerializer(data=request.data)
    
    if serializer.is_valid():
        if str(serializer.validated_data['priority']) == "HIGH" or str(serializer.validated_data['priority']) == "MEDIUM" or str(serializer.validated_data['priority']) == "LOW":
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response("priority should be: HIGH, MEDIUM, LOW",status=status.HTTP_428_PRECONDITION_REQUIRED)

@api_view(['PUT'])
def TaskUpdate(request,id,format=None):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def TaskDelete(request,id,format=None):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)