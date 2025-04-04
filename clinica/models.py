from django.db import models

escolhas = [
    ("CAR", "Cardiologista"),
    ("ORT", "Ortopedista"),
    ("SIR", "Sirurgiao"),
]

estatus = [
    ("AGD", "Agendado"),
    ("REA", "Realizado"),
    ("CAN", "Cancelado"),
]

class Medico(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True)
    especialidade = models.CharField(max_length=3, choices=escolhas)
    crm = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)


class Consulta(models.Model):
    paciente = models.CharField(max_length=30)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=estatus)
