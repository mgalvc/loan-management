# Generated by Django 4.2.2 on 2023-06-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proposal',
            options={'verbose_name': 'Proposta'},
        ),
        migrations.AlterModelOptions(
            name='proposalfield',
            options={'verbose_name': 'Campo'},
        ),
        migrations.AlterField(
            model_name='proposal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='metadata',
            field=models.JSONField(verbose_name='Campos'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='status',
            field=models.CharField(choices=[('P', 'Pendente'), ('A', 'Aprovado'), ('D', 'Negado')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='proposalfield',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='Habilitado'),
        ),
        migrations.AlterField(
            model_name='proposalfield',
            name='field_name',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
    ]
