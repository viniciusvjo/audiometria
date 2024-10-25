from os import error
from django.forms import ValidationError
from django.db import models
from datetime import date, timedelta
from utils.validar_cpf import valida_cpf


class Paciente(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    endereco = models.CharField(max_length=100, blank=True, null=True, verbose_name='Endereço')
    #cidade
    #estado
    #celular
    #email

    def calcular_idade(self) -> int:
        idade = (date.today() - self.data_nascimento) // timedelta(days=365.2425)
        return idade

    def __str__(self):
        return self.nome

    def clean(self):
        error_messages = {}
        cpf_enviado = self.cpf
        cpf_salvo = None
        paciente = Paciente.objects.filter(cpf=cpf_enviado).first()

        if paciente:
            cpf_salvo = paciente.cpf

            if cpf_salvo is not None and self.pk != paciente.pk:
                error_messages['cpf'] = 'CPF já existe'

        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'