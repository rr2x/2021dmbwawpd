from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World')


def anotherlink(request):
    return HttpResponse('Hello Again')


def item(request):
    return HttpResponse('<h1>This is an item view</h1>')
