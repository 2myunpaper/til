from django.urls import path, include
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create_todo, name='create_todo'),
    path('<int:todo_pk>', views.detail, name='detail'),
    path('<int:todo_pk>/edit_todo', views.edit_todo, name='edit_todo'),
    path('<int:todo_pk>/update', views.update_todo, name='update_todo'),
    path('<int:todo_pk>/delete', views.delete_todo, name='delete_todo'),
]