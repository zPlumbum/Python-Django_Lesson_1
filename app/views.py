from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    message = f'Текущее время: {current_time}'
    return HttpResponse(message)


def workdir_view(request):
    cwd_path = os.getcwd()
    cwd_files = os.listdir(cwd_path)
    message = f'В Вашей рабочей директории находятся следующие файлы: {cwd_files}'
    return HttpResponse(message)
