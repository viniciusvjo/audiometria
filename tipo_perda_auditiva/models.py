from django.db import models


# Create your models here.


class Tipo(models.Model):
    tipo_perda = models.CharField(max_length=40)
    caracteristicas = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo_perda
