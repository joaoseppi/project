from django.shortcuts import render
from django.http import HttpResponse


def my_mess(request):
    return HttpResponse('MEU OVO')


def home(request):
    return render(request, 'recipes/home.html')
    # return HttpResponse('HOME')


def sobre(request):
    return HttpResponse('CONTATO')


def contato(request):
    return HttpResponse('CONTATO')
