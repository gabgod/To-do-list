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
        
        ## validates the format for the inserted date for estimated time the wanted format is HH:MM
        if len(serializer.validated_data['estimated_time']) <=4 or ":" not in str(serializer.validated_data['estimated_time']): 
            return Response("estimated_time should be HH:MM ",status=status.HTTP_428_PRECONDITION_REQUIRED)

        ## validates the format for the inserted date for worked time the wanted format is HH:MM
        if len(serializer.validated_data['worked_time']) <=4 or ":" not in str(serializer.validated_data['worked_time']):
            return Response("worked_time should be HH:MM ",status=status.HTTP_428_PRECONDITION_REQUIRED)
        
        ## validates if the priority is recived is one of the predetermined options
        if str(serializer.validated_data['priority']) not in ["HIGH","MEDIUM","LOW"]:
            return Response("priority should be: HIGH, MEDIUM, LOW",status=status.HTTP_428_PRECONDITION_REQUIRED)

        ## if everything is alright the recived data is saved on the database
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def TaskUpdate(request,id,format=None):
    ## validates if the recived id correspond to a task id
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ## serialize the recived data and only updates what has been change, for a complete update change partial=False
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