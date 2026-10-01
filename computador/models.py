from django.db import models
from django.contrib.auth.models import User


class Computador(models.Model):
    
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class pecasDeComputador(models.Model):
    computador = models.ForeignKey(Computador,on_delete=models.CASCADE)
    
    processador = models.CharField(max_length=100, blank=True)
    placaMae = models.CharField(max_length=100, blank=True)
    memoriaRam = models.CharField(max_length=100, blank=True)
    armazenamento = models.CharField(max_length=100, blank=True)
    placaDeVideo = models.CharField(max_length=100, blank=True)
    fonte = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"Peças - {self.computador.nome}"
