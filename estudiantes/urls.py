from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_estudiante, name='create_estudiante'),
    path('list/', views.list_estudiantes, name='list_estudiantes'),
    path('<str:id>/', views.get_estudiante, name='get_estudiante'),
    path('<str:id>/update/', views.update_estudiante, name='update_estudiante'),
    path('<str:id>/delete/', views.delete_estudiante, name='delete_estudiante'),
]
