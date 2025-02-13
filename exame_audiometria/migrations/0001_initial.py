# Generated by Django 5.0.6 on 2024-08-21 22:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0002_alter_paciente_options_alter_paciente_cpf_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExameAudiometria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_exame', models.DateTimeField(verbose_name='Data do exame')),
                ('tipo_exame', models.CharField(choices=[(None, '(Selecione o tipo do exame)'), ('AD', 'Admissional'), ('PE', 'Periódico'), ('DE', 'Demissional'), ('SM', '6º Mês'), ('MF', 'Mudança de Função'), ('RT', 'Retorno ao Trabalho')], max_length=2)),
                ('od_via_aerea_250', models.SmallIntegerField(verbose_name='250')),
                ('od_via_aerea_500', models.SmallIntegerField(verbose_name='500')),
                ('od_via_aerea_1000', models.SmallIntegerField(verbose_name='1000')),
                ('od_via_aerea_2000', models.SmallIntegerField(verbose_name='2000')),
                ('od_via_aerea_3000', models.SmallIntegerField(verbose_name='3000')),
                ('od_via_aerea_4000', models.SmallIntegerField(verbose_name='4000')),
                ('od_via_aerea_6000', models.SmallIntegerField(verbose_name='6000')),
                ('od_via_aerea_8000', models.SmallIntegerField(verbose_name='8000')),
                ('od_via_ossea_250', models.SmallIntegerField(verbose_name='250')),
                ('od_via_ossea_500', models.SmallIntegerField(verbose_name='500')),
                ('od_via_ossea_1000', models.SmallIntegerField(verbose_name='1000')),
                ('od_via_ossea_2000', models.SmallIntegerField(verbose_name='2000')),
                ('od_via_ossea_3000', models.SmallIntegerField(verbose_name='3000')),
                ('od_via_ossea_4000', models.SmallIntegerField(verbose_name='4000')),
                ('od_via_ossea_6000', models.SmallIntegerField(verbose_name='6000')),
                ('od_via_ossea_8000', models.SmallIntegerField(verbose_name='8000')),
                ('od_sequencial_referencial', models.CharField(choices=[('S', 'Sequencial'), ('R', 'Referencial')], max_length=1, verbose_name='Sequencial/Referencial')),
                ('od_diagnostico_nosologico', models.CharField(choices=[(None, '(Selecione o diagnóstico nosológico)'), ('NO', 'Normal'), ('PA', 'PAO'), ('PN', 'PANO')], max_length=2, verbose_name='Diagnóstico nosológico')),
                ('od_diagnostico_evolutivo', models.CharField(choices=[(None, '(Selecione o diagnóstico evolutivo)'), ('NO', 'Normal'), ('ES', 'Estável'), ('SP', 'Sugestivo de Painpse'), ('AP', 'Agravamento de Painpse'), ('DP', 'Desencadeamento  de Painpse'), ('NP', 'Não Sugestivo  de Painpse')], max_length=2, verbose_name='Diagnóstico evolutivo')),
                ('oe_via_aerea_250', models.SmallIntegerField(verbose_name='250')),
                ('oe_via_aerea_500', models.SmallIntegerField(verbose_name='500')),
                ('oe_via_aerea_1000', models.SmallIntegerField(verbose_name='1000')),
                ('oe_via_aerea_2000', models.SmallIntegerField(verbose_name='2000')),
                ('oe_via_aerea_3000', models.SmallIntegerField(verbose_name='3000')),
                ('oe_via_aerea_4000', models.SmallIntegerField(verbose_name='4000')),
                ('oe_via_aerea_6000', models.SmallIntegerField(verbose_name='6000')),
                ('oe_via_aerea_8000', models.SmallIntegerField(verbose_name='8000')),
                ('oe_via_ossea_250', models.SmallIntegerField(verbose_name='250')),
                ('oe_via_ossea_500', models.SmallIntegerField(verbose_name='500')),
                ('oe_via_ossea_1000', models.SmallIntegerField(verbose_name='1000')),
                ('oe_via_ossea_2000', models.SmallIntegerField(verbose_name='2000')),
                ('oe_via_ossea_3000', models.SmallIntegerField(verbose_name='3000')),
                ('oe_via_ossea_4000', models.SmallIntegerField(verbose_name='4000')),
                ('oe_via_ossea_6000', models.SmallIntegerField(verbose_name='6000')),
                ('oe_via_ossea_8000', models.SmallIntegerField(verbose_name='8000')),
                ('oe_sequencial_referencial', models.CharField(choices=[('S', 'Sequencial'), ('R', 'Referencial')], max_length=1, verbose_name='Sequencial/Referencial')),
                ('oe_diagnostico_nosologico', models.CharField(choices=[(None, '(Selecione o diagnóstico nosológico)'), ('NO', 'Normal'), ('PA', 'PAO'), ('PN', 'PANO')], max_length=2, verbose_name='Diagnóstico nosológico')),
                ('oe_diagnostico_evolutivo', models.CharField(choices=[(None, '(Selecione o diagnóstico evolutivo)'), ('NO', 'Normal'), ('ES', 'Estável'), ('SP', 'Sugestivo de Painpse'), ('AP', 'Agravamento de Painpse'), ('DP', 'Desencadeamento  de Painpse'), ('NP', 'Não Sugestivo  de Painpse')], max_length=2, verbose_name='Diagnóstico evolutivo')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='paciente.paciente')),
            ],
        ),
    ]
