from django.db import models
from django.contrib.auth.models import User
import uuid
from pessoa.models import Pessoa
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

# Create your models here.

class Veiculo(models.Model):
    TIPO_VEICULO = (
        ('carro', 'Carro'),
        ('moto', 'Moto')
    )
    STATUS = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo')
    )
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    proprietario = models.ForeignKey(Pessoa, null=True, blank=False, on_delete=models.SET_NULL)
    tipo = models.CharField(max_length=5, choices=TIPO_VEICULO, null=False, blank=False)
    placa = models.CharField(max_length=8, null=False, blank=False)
    cor = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    ano = models.PositiveIntegerField(null=False, blank=False,
        default=current_year(), validators=[MinValueValidator(1960), max_value_current_year])
    data = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=7, choices=STATUS, null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        if self.tipo == 'carro':
            return self.cor
        else:
            return self.modelo
