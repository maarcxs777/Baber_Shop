from django.db import models

class Agendamento(models.Model):
    barbeiro = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return self.barbeiro