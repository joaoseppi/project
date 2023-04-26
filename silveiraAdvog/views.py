from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    return render(request, 'silveiraAdvog/pages/test.html')
    # return HttpResponse('HOME')
