from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_view(request: WSGIRequest):
    print(f"Method = {request.method}")
    print(f"GET DATA = {request.GET}")
    print(f"get data = {request.GET.get('name', 5)}")
    first = int(request.GET.get('first', 0))
    second = int(request.GET.get('second', 0))

    return render(request, 'index.html', context={'result': first + second})



