from django.shortcuts import render,HttpResponse
from .models import Contatos

def contatos(request):
    if request.method =='GET':
        return render(request, 'html/contatos.html')
    else:
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')

        contatos = Contatos(nome=nome, telefone=telefone, email=email)
        contatos.save()

        return render(request, 'html/parceiro.html')