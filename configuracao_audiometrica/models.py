from django.db import models


class ConfiguracaoAudiometrica(models.Model):
    tipo = models.CharField(max_length=40, null=False, blank=False)
    caracteristicas = models.TextField(max_length=200, verbose_name='Características')

    def __str__(self):
        return self.tipo
