from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='base'),
    path('tasks/', views.taskList, name='task-list'),
    path('tasks/<int:id>/', views.taskDetail, name='task-detail'),
    path('tasks/create/', views.taskCreate, name='task-create'),
    path('tasks/<int:id>/update/', views.taskUpdate, name='task-update'),
    path('tasks/<int:id>/delete/', views.taskDelete, name='task-delete'),

]