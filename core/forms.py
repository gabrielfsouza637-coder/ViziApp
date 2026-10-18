from django import forms
from .models import Prestador

class PrestadorForm(forms.ModelForm):
    class Meta:
        model = Prestador
        fields = ['nome', 'cpf', 'email', 'senha', 'whatsapp', 'horario']
        widgets = {
            'senha': forms.PasswordInput(attrs={'placeholder': 'Digite a senha'}),
        }

class PrestadorEditarForm(forms.ModelForm):
    senha_confirmacao = forms.CharField(
        label="Senha Atual para Confirmar Alterações",
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha atual'}),
        required=True
    )

    class Meta:
        model = Prestador
        fields = ['nome', 'email', 'whatsapp', 'horario']

    def clean_senha_confirmacao(self):
        senha_digitada = self.cleaned_data.get('senha_confirmacao')
        if self.instance and senha_digitada != self.instance.senha:
            raise forms.ValidationError("Senha incorreta! As alterações não foram salvas.")
        return senha_digitada