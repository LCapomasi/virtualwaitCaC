# Generated by Django 4.2.13 on 2024-07-12 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('dni', models.CharField(max_length=20)),
                ('sexo', models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino'), ('Otro', 'Otro')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('operacion', models.CharField(choices=[('cardiología', 'Cardiología'), ('clinicamedica', 'Clínica Médica'), ('dermatologia', 'Dermatología'), ('ginecologia', 'Ginecología'), ('hepatologia', 'Hepatología'), ('oftalmologia', 'Ofatalmología'), ('otorrinolaringologia', 'Otorrinolaringología'), ('traumatologia', 'Traumatología'), ('urologia', 'Urología')], max_length=20)),
                ('fecha', models.DateField()),
                ('motivo', models.TextField()),
                ('terminos', models.BooleanField()),
            ],
        ),
    ]
