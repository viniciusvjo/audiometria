from django.db import models

# Create your models here.


class GrauPerda(models.Model):
    grau_perda = models.CharField(max_length=40, null=False, blank=False, verbose_name='Grau de perda auditiva')
    media_frequencias = models.CharField(max_length=15, null=False, blank=False, verbose_name='Média entre as frequências de 500 Hz, 1 kHz, 2 kHz e 4 kHz')
    desempenho = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.grau_perda
