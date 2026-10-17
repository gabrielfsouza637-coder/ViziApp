from django.shortcuts import render, redirect
from .models import Prestador
from .models import models
from .models import Servico
from .models import Solicitacao
from .forms import PrestadorForm
from django.shortcuts import render, get_object_or_404, redirect

def inicial(request):
    contexto = {
        'titulo': 'Bem-vindo ao ViziApp'
    }

    return render(request, 'tela-inicial.html', contexto)

def listar_servicos(request):
    servicos = Servico.objects.all()
    contexto = {
        'servicos': servicos
    }
    return render(request, 'tela-de-serviços.html', contexto)

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

def cadastrar_servico(request):
    form = PrestadorForm(request.POST or None)

    if form.is_valid():
        form.save()  
        return redirect('listar_prestadores')

    contexto = {
        'form_prestador': form
    }
    return render(request, 'cadastrar-serviços.html', contexto)

def listar_prestadores(request):
    prestadores = Prestador.objects.all() 
    contexto = {
        'prestadores': prestadores
    }
    return render(request, 'prestadores.html', contexto)