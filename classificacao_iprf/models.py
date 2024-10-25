from django.db import models


class ClassificacaoIPRF(models.Model):
    resultado = models.CharField(max_length=20, null=False, blank=False, verbose_name='Resultado de IPRF')
    dificuldade = models.CharField(max_length=100, verbose_name='Dificuldade de compreensão da fala')

    def __str__(self):
        return self.resultado
