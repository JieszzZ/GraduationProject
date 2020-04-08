from django.shortcuts import render
from django.http import HttpResponse

import docker


# Create your views here.

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def msg(request):
    client = docker.APIClient('tcp://localhost:2375')
    print(client.version())
    return HttpResponse(client.version())