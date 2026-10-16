from django.db import models
class Prestador(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=20)
    horario = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nome

class Morador(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE, related_name='servicos')

    def __str__(self):
        return self.nome

class Solicitacao(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE, related_name='solicitacoes')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='solicitacoes')

    def __str__(self):
        return f"Solicitação #{self.id} - {self.morador.nome}"
