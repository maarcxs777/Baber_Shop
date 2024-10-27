from django.shortcuts import render,HttpResponse
from .models import Agendamento

def agendamento(request):
    if request.method == 'GET':
        return render(request, 'html/agendamento.html')
    else:
        barbeiro = request.POST.get('barbeiro')
        nome = request.POST.get('nome')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        agendamento = Agendamento(barbeiro=barbeiro, nome=nome, data=data, hora=hora)
        agendamento.save()

        return render(request, 'html/agendado.html')
