from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return HttpResponse('LOGIN PAGE')


def register(request):
    return HttpResponse('REGISTER PAGE')


def logout(request):
    return HttpResponse('LOGOUT PAGE')
