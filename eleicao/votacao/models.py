from django.db import models
from django.contrib.auth.models import User
class Eleicao(models.Model):
    HoraDataI = models.DateTimeField(blank=True, null=True)
    HoraDataF = models.DateTimeField(blank=True, null=True)
    local = models.CharField(max_length=128)
    
    def __str__(self):
        return self.local

class Eleitor(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=11)
    eleicao= models.ForeignKey(Eleicao, null=True, blank=False)

    def __str__(self):
        return self.nome 
class Vaga (models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
class Candidato(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=11)
    propostas = models.TextField()
    vaga= models.ForeignKey(Vaga, null=True, blank=False)

    def __str__(self):
        return self.nome
class Urna (models.Model):
    candidato= models.ForeignKey(Candidato, null=True, blank=False)
    votos=  models.IntegerField(max_length=10)
    branco= models.CharField(max_length=128)
    def __str__(self):
        return self.votou
class Token(models.Model):
    token = models.CharField(max_length=128)
    urna = models.ForeignKey(Urna, null=True, blank=False)
    eleitor=models.OneToOneField(Eleitor)

    def __str__(self):
        return self.token