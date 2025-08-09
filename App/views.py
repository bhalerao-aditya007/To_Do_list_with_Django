from django.shortcuts import redirect
from . models import Task

# Create your views here.
def addTask(request):
    if request.method == 'POST':
        task_value = request.POST.get('task','').strip()
        if task_value:
            Task.objects.create(task = task_value)
        return redirect ('home')
    
    