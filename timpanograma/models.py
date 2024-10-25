from django.db import models


class Timpanograma(models.Model):
    tipo = models.CharField(max_length=10, null=False, blank=False, verbose_name='Tipo da curva')
    definicao = models.CharField(max_length=100, verbose_name='Definição')
    valor_referencia = models.CharField(max_length=200, null=True, blank=True, verbose_name='Valor de referência')

    def __str__(self):
        return self.tipo
