# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-06-16 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('idade', models.IntegerField()),
                ('nascimento', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('cidade', models.CharField(max_length=30)),
            ],
        ),
    ]
