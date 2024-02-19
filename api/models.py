from django.db import models

# Create your models here.


class Task(models.Model):
    task_title =  models.CharField(max_length=200)
    task_description = models.TextField()
    estimated_time = models.FloatField(null=True,blank=True)
    worked_time = models.FloatField(null=True,blank=True)
    status = models.BooleanField(verbose_name='completed', default=False)
    priority = models.CharField(max_length=6,default="HIGH")
    #Why not on_delete=models.CASCADE, a owner could be fired but the task should still be completed
    
    '''
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT,
        related_name='owner'
    )

    assignee = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT,
        related_name='assignee'
    )

    priority = models.ForeignKey(
        Priority,
        on_delete=models.PROTECT
    )
    '''
    def __str__(self):
        return self.task_title