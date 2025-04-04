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
    crm = models.CharField(max_length=7)
    email = models.EmailField(max_length=30, default='DEFAULT VALUE', null=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.CharField(max_length=30)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=estatus)

    def __str__(self):
        return self.paciente
