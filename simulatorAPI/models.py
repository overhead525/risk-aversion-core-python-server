import uuid
from django.db import models


class Configuration(models.Model):
    simID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    principal = models.FloatField(max_length=15)
    riskDecimal = models.FloatField(max_length=5)
    rewardDecimal = models.FloatField(max_length=5)
    winDecimal = models.FloatField(max_length=5)
    lossDecimal = models.FloatField(max_length=5)
    breakEvenDecimal = models.FloatField(max_length=5)
    numOfTrades = models.IntegerField()
    numOfSimulations = models.IntegerField()

    def __str__(self):
        return f'Simulation ID:{self.simID}'


class SimulationResult(models.Model):
    simID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    maxPortfolio = models.FloatField(max_length=15)
    minPortfolio = models.FloatField(max_length=15)

    def __str__(self):
        return f'Simulation ID:{self.simID}'
