from django.db import models

# Create your models here.
class Turno(models.Model):
    SEXO_CHOICES = [
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
        ('Otro', 'Otro'),
    ]

    OPERACION_CHOICES = [
        ('cardiología', 'Cardiología),
        ('clinicamedica','Clínica Médica'),
        ('dermatologia','Dermatología'),
        ('ginecologia','Ginecología'),
        ('hepatologia','Hepatología'),
        ('oftalmologia','Ofatalmología'),
        ('otorrinolaringologia','Otorrinolaringología'),
        ('traumatologia','Traumatología'),
        ('urologia','Urología') 
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    dni = models.CharField(max_length=20)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    email = models.EmailField()
    operacion = models.CharField(max_length=20, choices=OPERACION_CHOICES)
    fecha = models.DateField()
    motivo = models.TextField()
    terminos = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.operacion}"
