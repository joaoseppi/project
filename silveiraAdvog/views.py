from django.shortcuts import render
from django.http import HttpResponse


def my_mess(request):
    return HttpResponse('MEU OVO')


def home(request):
    return render(request, 'silveiraAdvog/home.html')
    # return HttpResponse('HOME')