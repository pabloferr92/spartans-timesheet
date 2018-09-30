# Generated by Django 2.1.1 on 2018-09-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(blank=True, max_length=5000, null=True)),
                ('criado_por', models.CharField(max_length=100)),
                ('data_criacao', models.DateTimeField()),
                ('atualizado_por', models.CharField(max_length=100)),
                ('data_ultima_atualizacao', models.DateTimeField()),
            ],
            options={
                'db_table': 'categoria',
                'managed': False,
            },
        ),
    ]
