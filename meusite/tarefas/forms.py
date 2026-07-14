from django import forms
from .models import TarefaModel

class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ['assunto','descricao','status']