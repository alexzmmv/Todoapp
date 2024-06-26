from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('todo/delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('todo/status/<int:todo_id>/', views.status_todo, name='status_todo'),
]