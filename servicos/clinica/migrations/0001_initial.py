# Generated by Django 4.2 on 2025-04-04 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=30, null=True)),
                ('especialidade', models.CharField(choices=[('CAR', 'Cardiologista'), ('ORT', 'Ortopedista'), ('SIR', 'Sirurgiao')], max_length=3)),
                ('crm', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=30)),
                ('data', models.DateTimeField()),
                ('status', models.CharField(choices=[('AGD', 'Agendado'), ('REA', 'Realizado'), ('CAN', 'Cancelado')], max_length=3)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.medico')),
            ],
        ),
    ]
