from django.urls import path
from .views import ContactsView, contacts_view, tasks_view, users_view, subtasks_view, contacts_single_view

urlpatterns = [
    path('users/', users_view),
    path('contacts/', ContactsView.as_view()),
    path('contacts/<int:pk>/', contacts_single_view),
    path('tasks/', tasks_view),
    path('subtasks/', subtasks_view),
]
