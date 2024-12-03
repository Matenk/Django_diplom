from dbm.dumb import error

from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request,'main/index.html',
                  {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Неверная форма'


    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)
