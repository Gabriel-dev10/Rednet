from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    latencia = models.PositiveIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

