from django.forms import ModelForm
from .models import Prestador


class PrestadorForm(ModelForm): 
    class Meta:
        model = Prestador
        fields = ['nome', 'cpf', 'email', 'senha', 'whatsapp', 'horario']