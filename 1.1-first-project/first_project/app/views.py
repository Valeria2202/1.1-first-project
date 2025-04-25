from django.shortcuts import render, reverse
from django.http import HttpResponse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def current_time_view(request):
    now = datetime.datetime.now()
    msg = f'Текущее время: {now.strftime("%Y-%m-%d %H:%M:%S")}'
    return HttpResponse(msg)

def workdir_view(request):
    files = os.listdir('.')  # Получаем список файлов в текущей директории
    file_list = "<ul>"
    for file in files:
        file_list += f"<li>{file}</li>"
    file_list += "</ul>"
    return HttpResponse(f"Содержимое рабочей директории:<br>{file_list}")