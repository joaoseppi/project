from django.shortcuts import render
from django.http import HttpResponse


def my_mess(request):
    return HttpResponse('MEU OVO')


def home(request):
    return render(request, 'recipes/home.html')
    # return HttpResponse('HOME')


def sobre(request):
    return render(request, 'recipes/contato.html')


def contato(request):
    return HttpResponse('CONTATO')
