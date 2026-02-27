from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = [
            'nome', 'cpf', 'estado_nascimento', 
            'cidade_nascimento', 'area_atuacao', 
            'crm', 'contato', 'email'
        ]

    widgets = {
            'cpf': forms.TextInput(attrs={'maxlength': '14', 'placeholder': '000.000.000-00'}),
            'contato': forms.TextInput(attrs={'maxlength': '15', 'placeholder': '(00) 00000-0000'}),
        }