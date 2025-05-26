from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import JsonResponse


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def criar_task(request):
    task = Task(title=request.POST['title'], description=request.POST['description'], bairro=request.POST['bairro'], latencia=int(request.POST['latencia']))
    task.save()
    return redirect('/tasks/')

def deletar_task(request,task_id):
    delete_task = Task.objects.get(id=task_id)
    delete_task.delete()
    return redirect('/tasks/')

def detalhar_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'detalhes.html', {'task': task})

def atualizar_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.bairro = request.POST.get('bairro')
        task.save()
        return redirect('/tasks/')

    return render(request, 'editar.html', {'task': task})

def exportar_latencia_json(request):
    tarefas = Task.objects.all().values('latencia')
    return JsonResponse(list(tarefas), safe=False)