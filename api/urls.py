from django.urls import path

from .views import TaskList,TaskAdd,TaskUpdate,TaskDelete

urlpatterns = [
    path('',TaskList,name='list'),
    path('add/',TaskAdd,name='add'),
    path('update/<int:id>',TaskUpdate,name='update'),
    path('delete/<int:id>',TaskDelete,name='delete')
]
