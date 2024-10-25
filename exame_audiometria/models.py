from django.db import models
from paciente.models import Paciente
from django.utils.translation import gettext_lazy as _


class ExameAudiometria(models.Model):
    class TipoExame(models.TextChoices):
        ADMISSIONAL = 'AD', _('Admissional')
        PERIODICO = 'PE', _('Periódico')
        DEMISSIONAL = "DE", _("Demissional")
        SEXTO_MES = 'SM', _('6º Mês')
        MUDANCA_FUNCAO = 'MF', _('Mudança de Função')
        RETORNO_TRABALHO = 'RT', _('Retorno ao Trabalho')
        __empty__ = _("(Selecione o tipo do exame)")

    class DiagnosticoNosologico(models.TextChoices):
        NORMAL = 'NO', _('Normal')
        PAO = 'PA', _('PAO')
        PANO = "PN", _("PANO")
        __empty__ = _("(Selecione o diagnóstico nosológico)")

    class DiagnosticoEvolutivo(models.TextChoices):
        NORMAL = 'NO', _('Normal')
        ESTAVEL = 'ES', _('Estável')
        SUGESTIVO_PAINPSE = "SP", _("Sugestivo de Painpse")
        AGRAVAMENTO_PAINPSE = 'AP', _('Agravamento de Painpse')
        DESENCADEAMENTO_PAINPSE = 'DP', _('Desencadeamento  de Painpse')
        NAO_SUGESTIVO_PAINPSE = 'NP', _('Não Sugestivo  de Painpse')
        __empty__ = _("(Selecione o diagnóstico evolutivo)")

    paciente = models.ForeignKey(Paciente, blank=False, null=False, on_delete=models.PROTECT)
    data_exame = models.DateTimeField(blank=False, null=False, verbose_name='Data do exame')
    tipo_exame = models.CharField(max_length=2, choices=TipoExame, blank=False, null=False)

    # Ouvido direito - Vias aéreas
    od_via_aerea_250 = models.SmallIntegerField(verbose_name='250')
    od_via_aerea_500 = models.SmallIntegerField(verbose_name='500')
    od_via_aerea_1000 = models.SmallIntegerField(verbose_name='1000')
    od_via_aerea_2000 = models.SmallIntegerField(verbose_name='2000')
    od_via_aerea_3000 = models.SmallIntegerField(verbose_name='3000')
    od_via_aerea_4000 = models.SmallIntegerField(verbose_name='4000')
    od_via_aerea_6000 = models.SmallIntegerField(verbose_name='6000')
    od_via_aerea_8000 = models.SmallIntegerField(verbose_name='8000')

    # Ouvido direito - Vias ósseas
    od_via_ossea_250 = models.SmallIntegerField(verbose_name='250')
    od_via_ossea_500 = models.SmallIntegerField(verbose_name='500')
    od_via_ossea_1000 = models.SmallIntegerField(verbose_name='1000')
    od_via_ossea_2000 = models.SmallIntegerField(verbose_name='2000')
    od_via_ossea_3000 = models.SmallIntegerField(verbose_name='3000')
    od_via_ossea_4000 = models.SmallIntegerField(verbose_name='4000')
    od_via_ossea_6000 = models.SmallIntegerField(verbose_name='6000')
    od_via_ossea_8000 = models.SmallIntegerField(verbose_name='8000')

    od_sequencial_referencial = models.CharField(max_length=1, choices=[('S', 'Sequencial'), ('R', 'Referencial')], verbose_name='Sequencial/Referencial')
    od_diagnostico_nosologico = models.CharField(max_length=2, choices=DiagnosticoNosologico, verbose_name='Diagnóstico nosológico')
    od_diagnostico_evolutivo =  models.CharField(max_length=2, choices=DiagnosticoEvolutivo, verbose_name='Diagnóstico evolutivo')

    # Ouvido esquerdo - Vias aéreas
    oe_via_aerea_250 = models.SmallIntegerField(verbose_name='250')
    oe_via_aerea_500 = models.SmallIntegerField(verbose_name='500')
    oe_via_aerea_1000 = models.SmallIntegerField(verbose_name='1000')
    oe_via_aerea_2000 = models.SmallIntegerField(verbose_name='2000')
    oe_via_aerea_3000 = models.SmallIntegerField(verbose_name='3000')
    oe_via_aerea_4000 = models.SmallIntegerField(verbose_name='4000')
    oe_via_aerea_6000 = models.SmallIntegerField(verbose_name='6000')
    oe_via_aerea_8000 = models.SmallIntegerField(verbose_name='8000')

    # Ouvido esquerdo - Vias ósseas
    oe_via_ossea_250 = models.SmallIntegerField(verbose_name='250')
    oe_via_ossea_500 = models.SmallIntegerField(verbose_name='500')
    oe_via_ossea_1000 = models.SmallIntegerField(verbose_name='1000')
    oe_via_ossea_2000 = models.SmallIntegerField(verbose_name='2000')
    oe_via_ossea_3000 = models.SmallIntegerField(verbose_name='3000')
    oe_via_ossea_4000 = models.SmallIntegerField(verbose_name='4000')
    oe_via_ossea_6000 = models.SmallIntegerField(verbose_name='6000')
    oe_via_ossea_8000 = models.SmallIntegerField(verbose_name='8000')

    oe_sequencial_referencial = models.CharField(max_length=1, choices=[('S', 'Sequencial'), ('R', 'Referencial')], verbose_name='Sequencial/Referencial')
    oe_diagnostico_nosologico = models.CharField(max_length=2, choices=DiagnosticoNosologico, verbose_name='Diagnóstico nosológico')
    oe_diagnostico_evolutivo = models.CharField(max_length=2, choices=DiagnosticoEvolutivo, verbose_name='Diagnóstico evolutivo')