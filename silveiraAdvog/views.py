from django.shortcuts import render
from django.http import HttpResponse


def my_mess(request):
    return HttpResponse('MEU OVO')


def home(request):
    return render(request, 'silveiraAdvog/home.html')
    # return HttpResponse('HOME')


def cadastro(request):
    return render(request, 'silveiraAdvog/cadastro.html')


def login(request):
    return render(request, 'silveiraAdvog/login.html')
