from django.urls import path
from .views import SubtaskDetailView, SubtasksView, TaskDetailView, TasksView, ContactDetailView, ContactsView, UsersView, UserDetailView

urlpatterns = [
    path('contacts/', ContactsView.as_view()),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('users/', UsersView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('tasks/', TasksView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    path('tasks/<int:task_id>/subtasks/', SubtasksView.as_view(), name='task-subtask-detail'),
    path('subtasks/', SubtasksView.as_view()),
    path('tasks/<int:task_id>/subtasks/<int:subtask_id>/', SubtaskDetailView.as_view(), name='subtask-detail'),    
]
