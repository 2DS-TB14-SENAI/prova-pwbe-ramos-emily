from django.db import models
from django.core.validators import RegexValidator, EmailValidator

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
    crm = models.CharField(
        max_length=8, 
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{2}/\d{5}$',
                message="CRM deve estar no formato XX/XXXXX, exemplo: SP/12345."
            )
        ]
    )
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator(message="Insira um e-mail válido.")]
    )

    def __str__(self):
        return f"{self.nome} - {self.crm}"
    


class Consulta(models.Model):
    paciente = models.CharField(max_length=30)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=estatus)

    def __str__(self):
        return self.paciente
