from django.db import models


class ReflexoAcustico(models.Model):
    tipo = models.CharField(max_length=1, choices=[('P', 'Presente'), ('A', 'Ausente')])
    descricao = models.CharField(max_length=80, null=False, blank=False, verbose_name='Descrição')
    caracteristicas = models.CharField(max_length=200, null=True, blank=True, verbose_name='Características')

    def __str__(self):
        return self.descricao
