from django.db import models
from django.contrib.auth.models import User


class Computador(models.Model):
    
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nome

class Processador(models.Model):
    processador = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.processador
    
class PlacaMae(models.Model):
    placaMae = models.CharField(max_length=100, blank=True)
    socket = models.CharField(max_length=30, blank=True, null=True)
    chipset = models.CharField(max_length=30, blank=True, null=True)
    tipo_memoria = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return f"{self.placaMae} | Socket: {self.socket} | ChipSet: {self.chipset} | Tipo de Memória: {self.tipo_memoria}"
    
class MemoriaRam(models.Model):
    memoriaRam = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.memoriaRam
    
class Armazenamento(models.Model):
    armazenamento = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.armazenamento
    
class PlacaDeVideo(models.Model):
    placaDeVideo = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.placaDeVideo
    
class Fonte(models.Model):
    fonte = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.fonte


class pecasDeComputador(models.Model):
    
    computador = models.OneToOneField(Computador,on_delete=models.CASCADE, related_name='pecas')
    processador = models.ForeignKey(Processador, on_delete=models.PROTECT)
    placaMae = models.ForeignKey(PlacaMae, on_delete=models.PROTECT)
    memoriaRam = models.ForeignKey(MemoriaRam, on_delete=models.PROTECT)
    armazenamento = models.ForeignKey(Armazenamento, on_delete=models.PROTECT)
    placaDeVideo = models.ForeignKey(PlacaDeVideo, on_delete=models.PROTECT)
    fonte = models.ForeignKey(Fonte, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Peças - {self.computador.nome}"
