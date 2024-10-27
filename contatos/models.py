from django.db import models

class Contatos(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.nome