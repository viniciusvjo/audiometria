# Generated by Django 5.0.6 on 2024-08-21 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timpanograma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timpanograma',
            name='definicao',
            field=models.CharField(max_length=100, verbose_name='Definição'),
        ),
        migrations.AlterField(
            model_name='timpanograma',
            name='tipo',
            field=models.CharField(max_length=10, verbose_name='Tipo da curva'),
        ),
        migrations.AlterField(
            model_name='timpanograma',
            name='valor_referencia',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Valor de referência'),
        ),
    ]
