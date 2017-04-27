from django.db import models

class Thermostat(models.Model):
    name = models.CharField(max_length=64, default='')
    zwave_id = models.IntegerField(default=-1)
