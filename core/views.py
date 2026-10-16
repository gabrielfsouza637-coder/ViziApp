from django.shortcuts import render
from .models import Prestador
from .models import models
from .models import Servico
from .models import Solicitacao

def inicial(request):
    servicos = Servico.objects.all()
    contexto = {
        'titulo': 'ViziApp - Serviços Comunitários',
        'servicos': servicos 
    }
    return render(request, 'tela-inicial.html', contexto)

def listar_categoria(request):
    servicos = Servico.objects.all()
    contexto = {
        'servicos': servicos
    }
    return render(request, 'tela-inicial.html', contexto)

def detalhe_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    contexto = {
        'servico': servico
    }
    return render(request, 'detalhe-servico.html', contexto)

def listar_prestadores(request):
    prestadores = Prestador.objects.all()
    contexto = {
        'prestadores': prestadores
    }
    return render(request, 'prestadores.html', contexto)
