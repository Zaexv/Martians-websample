from django.db import models


class nave_nodriza(models.Model):
    nombre = models.CharField(max_length=400)

class aeronave(models.Model):
    nombre = models.CharField(max_length=400)
    max_marcianos = models.IntegerField()
    nave_origen = models.ForeignKey(nave_nodriza, on_delete=models.CASCADE,
        related_name = 'nave_origen', null=True)
    nave_destino = models.ForeignKey(nave_nodriza, on_delete=models.CASCADE,
        related_name = 'nave_destino', null=True)
