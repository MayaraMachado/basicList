from django import forms
from .models import Produtos

class ProdutoForm (forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'quantidade']

class BuscaForm(forms.Form):
    produto = forms.CharField(max_length = 50)
