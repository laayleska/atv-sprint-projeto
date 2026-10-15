from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'data_inicio']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do Projeto'}),
            'descricao': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descrição do Projeto'}),
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
        }