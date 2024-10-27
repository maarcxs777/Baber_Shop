from django.shortcuts import render,HttpResponse

def cadastro(request):
    return HttpResponse('Cadastro')

def login(request):
    return HttpResponse('Login')

def redefinir(request):
    return HttpResponse('Redefinir')