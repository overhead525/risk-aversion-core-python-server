import asyncio
import graphene
from graphene_django import DjangoObjectType
from django.db.models import QuerySet
from typing import List

from .models import SimulationResult, Configuration

from .helpers.SimulationHandler import executeSimulation


class SimulatorConfiguration(graphene.ObjectType):
    principal = graphene.Float()
    riskDecimal = graphene.Float()
    rewardDecimal = graphene.Float()
    winDecimal = graphene.Float()
    lossDecimal = graphene.Float()
    breakEvenDecimal = graphene.Float()
    numOfTrades = graphene.Int()
    numOfSimulations = graphene.Int()


class SimulationType(DjangoObjectType):
    class Meta:
        model = SimulationResult


class SimulationMutation(graphene.Mutation):
    class Input:
        principal = graphene.Float()
        riskDecimal = graphene.Float()
        rewardDecimal = graphene.Float()
        winDecimal = graphene.Float()
        lossDecimal = graphene.Float()
        breakEvenDecimal = graphene.Float()
        numOfTrades = graphene.Int()
        numOfSimulations = graphene.Int()

    result = graphene.Field(SimulationType)

    def mutate(
            self,
            info,
            principal,
            riskDecimal,
            rewardDecimal,
            winDecimal,
            lossDecimal,
            breakEvenDecimal,
            numOfTrades,
            numOfSimulations
    ):
        result = executeSimulation(
            principal,
            riskDecimal,
            rewardDecimal,
            winDecimal,
            lossDecimal,
            breakEvenDecimal,
            numOfTrades,
            numOfSimulations
        )
        return SimulationMutation(result=result)


class DeleteSingleSimulation(graphene.Mutation):
    class Arguments:
        simID = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, simID):
        simulationResultDeletion = SimulationResult.objects.filter(simID=simID).delete()
        configurationDeletion = Configuration.objects.filter(simID=simID).delete()
        if simulationResultDeletion[0] > 0 and configurationDeletion[0] > 0:
            ok = True
        else:
            ok = False
        return DeleteSingleSimulation(ok=ok)


class DeleteMultipleSimulations(graphene.Mutation):
    class Arguments:
        simIDs = graphene.List(graphene.String)

    ok = graphene.List(graphene.Boolean)

    def mutate(self, info, simIDs: List[str]):
        ok = []
        for simID in simIDs:
            simulationResultDeletion = SimulationResult.objects.filter(simID=simID).delete()
            configurationDeletion = Configuration.objects.filter(simID=simID).delete()
            if simulationResultDeletion[0] > 0 and configurationDeletion[0] > 0:
                ok.append(True)
            else:
                ok.append(False)
        return DeleteMultipleSimulations(ok=ok)


class Mutation(graphene.ObjectType):
    simulate = SimulationMutation.Field()
    deleteSingleSimulation = DeleteSingleSimulation.Field()
    deleteMultipleSimulations = DeleteMultipleSimulations.Field()
