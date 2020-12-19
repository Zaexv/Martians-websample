from django.db import models


class nave_nodriza(models.Model):
    nombre = models.CharField(max_length=400)

class aeronave(models.Model):
    nombre = models.CharField(max_length=400)
    max_marcianos = models.PositiveIntegerField()
    nave_origen = models.ForeignKey(nave_nodriza, on_delete=models.CASCADE,
        related_name = 'nave_origen', null=True)
    nave_destino = models.ForeignKey(nave_nodriza, on_delete=models.CASCADE,
        related_name = 'nave_destino', null=True)

class Pasajero(models.Model):
    nombre = models.CharField(max_length=400)
    aeronave_id = models.ForeignKey(aeronave, on_delete=models.CASCADE,
        related_name = 'subido_en', null=True, blank=True)

class Revision(models.Model):
    nombre_revisor = models.CharField(max_length=400)
    aeronave_id = models.ForeignKey(aeronave, on_delete=models.CASCADE,
        related_name = 'revisa_a', null=True, blank=True)
    num_pasajeros = models.IntegerField()
    fecha_revision = models.DateField()
