import asyncio
import graphene
from graphene_django import DjangoObjectType

from .models import SimulationResult

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


class Mutation(graphene.ObjectType):
    simulate = SimulationMutation.Field()
