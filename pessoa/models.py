from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.fields import AutoField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Pessoa(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, blank=False, null=False)
    documento = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=500, blank=False, null=False)
    telefone = PhoneNumberField(null=False, blank=False)
    data = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.nome
