import sys
import os

from django.urls import path
from django.core.management import execute_from_command_line
from django.shortcuts import render


def index(request):
    message = request.GET.get("message", "")
    return render(request, "template.html", 
                  {"message": message})
                 # {"message": '<img src="https://icdn.lenta.ru/images/2024/01/20/13/20240120130809407/preview_2591164ece7f78adf94d69dcf105ba8a.jpg">'})


urlpatterns = [
    path(r'', index),
]

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    execute_from_command_line(sys.argv)
