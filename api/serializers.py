from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    #owner = serializers.SerializerMethodField()
    #assignee = serializers.SerializerMethodField()
    #priority = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id','task_title','task_description','estimated_time','worked_time','status','priority']

    '''
    def get_owner(self,obj):
        return obj.owner.username

    def get_assignee(self,obj):
        return obj.assignee.username
    
    def get_priority(self,obj):
        return obj.priority.priority_level
    '''