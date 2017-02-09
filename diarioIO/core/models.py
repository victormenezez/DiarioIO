from django.db import models
from django.contrib.auth.models import User


class Diario(models.Model):
    autor = models.ForeignKey(User, default=None)
    data = models.DateField()
    hora_chegada = models.TimeField()
    objetivos = models.TextField()
    materiais_metodos = models.TextField(blank=True, null=True)
    resultados = models.TextField()
    avaliacao = models.TextField(default="")
    atividades_futuras = models.TextField(blank=True, null=True)
    bibliografia = models.TextField(blank=True, null=True)
    hora_saida = models.TimeField()

    def __str__(self):
        return self.autor.first_name + " - " + str(self.data)
