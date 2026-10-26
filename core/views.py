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

def editar_prestador(request, id):
    prestador = get_object_or_404(Prestador, id=id)
    form = PrestadorForm(request.POST or None, instance=prestador)
    if form.is_valid():
        form.save()
        return redirect('listar_prestadores')
    contexto = {
        'form_prestador': form
    }
    return render(request, 'cadastrar-serviços.html', contexto)

def remover_prestador(request, id):
    prestador = get_object_or_404(Prestador, id=id)
    prestador.delete()
    return redirect('listar_prestadores')

def login(request):
    erro = None
    
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            # Aqui é a função que procura o prestador cadastrado pelo e-mail
            prestador = Prestador.objects.get(email=email)
            
            # Aqui esta a validação se a senha informada é igual à salva no banco
            if prestador.senha == senha:
                # Aqui está a validação se o ID do prestador na sessão do navegador
                request.session['prestador_id'] = prestador.id
                return redirect('listar_prestadores')
            else:
                erro = "Senha incorreta. Tente novamente."
        except Prestador.DoesNotExist:
            erro = "E-mail não encontrado no sistema."

    contexto = {
        'erro': erro
    }
    return render(request, 'login.html', contexto)
