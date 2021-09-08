from django.forms import ModelForm
from django import forms
from .models import Pessoa

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['user', 'nome', 'email', 'telefone', 'documento']

    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})