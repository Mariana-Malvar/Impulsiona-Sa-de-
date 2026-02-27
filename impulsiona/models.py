from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    estado_nascimento = models.CharField(max_length=2)
    cidade_nascimento = models.CharField(max_length=100)
    area_atuacao = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, blank=True, null=True)
    contato = models.CharField(max_length=15)
    email = models.EmailField()


