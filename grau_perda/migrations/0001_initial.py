# Generated by Django 5.0.6 on 2024-06-26 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrauPerda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuracao_audiometrica', models.CharField(max_length=40)),
                ('media_frequencias', models.CharField(max_length=15)),
                ('desempenho', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
