from django.shortcuts import render
from App.models import Task
def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    completed = Task.objects.filter(is_completed = True).order_by('-updated_at')
    context = {
        'tasks': tasks,
        'completed':completed,
    }
    return render (request, 'home.html', context)