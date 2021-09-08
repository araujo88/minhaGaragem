from django.forms import ModelForm
from django import forms
from django.http import request
from .models import Veiculo
from .models import Pessoa

class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['user', 'proprietario', 'tipo', 'cor', 'modelo', 'ano', 'placa', 'status']

    def __init__(self, user, *args, **kwargs):
        super(VeiculoForm, self).__init__(*args, **kwargs)
        self.fields['proprietario'].queryset = Pessoa.objects.filter(user=user)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})