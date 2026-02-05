from django.urls import path 
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"), 
    path('api/v1/projects/', views.getProjects, name="projects"),
    path('api/v1/projects/<str:pk>/', views.getProject, name="project"),        
    path('api/v1/projects/create/', views.createProject, name="create-project"),
    path('api/v1/projects/<str:pk>/task/create/', views.createTask, name="create-task"),                
    path('api/v1/users/', views.getUsers, name="users"),
    path('api/v1/users/create/', views.createUser, name="create-user"),     
]