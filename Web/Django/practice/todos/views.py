from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

def new(request):
    return render(request, 'todos/new.html')

def create_todo(request):
    work = request.POST.get('work')
    content = request.POST.get('content')

    todo = Todo(work=work, content=content, is_completed=False)
    todo.save()
    return redirect('todos:detail', todo.pk)

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/detail.html', context)

def edit_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/edit.html', context)

def update_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.work = request.POST.get('work')
    todo.content = request.POST.get('content')
    todo.save()
    return redirect('todos:detail', todo.pk)

def delete_todo(request, todo_pk):
    Todo.objects.get(pk=todo_pk).delete()
    return redirect('todos:index')