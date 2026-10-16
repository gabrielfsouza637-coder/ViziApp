from django.db import models

from django.db import models

class Prestador(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=20)
    horario = models.CharField(max_length=100, blank=True, null=True)
