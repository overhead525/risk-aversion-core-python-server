import graphene
from graphene_django import DjangoObjectType
from django.db.models import QuerySet

from .models import Configuration, SimulationResult


class ConfigurationType(DjangoObjectType):
    class Meta:
        model = Configuration
        fields = (
            "principal",
            "riskDecimal",
            "rewardDecimal",
            "winDecimal",
            "lossDecimal",
            "breakEvenDecimal",
            "numOfTrades",
            "numOfSimulations"
        )


class SimulationResultType(DjangoObjectType):
    class Meta:
        model = SimulationResult
        fields = (
            "simID",
            "maxPortfolio",
            "minPortfolio"
        )


class Query(graphene.ObjectType):
    all_configurations = graphene.List(ConfigurationType)
    configuration_by_id = graphene.Field(ConfigurationType, simID=graphene.String(required=True))

    all_simulation_results = graphene.List(SimulationResultType)
    simulation_result_by_id = graphene.Field(SimulationResultType, simID=graphene.String(required=True))

    def resolve_all_configurations(self, info):
        return Configuration.objects.all()

    def resolve_configuration_by_id(self, info, simID):
        objects: QuerySet = Configuration.objects.filter(simID=simID)
        if objects.count() == 0:
            return None
        return objects[0]

    def resolve_all_simulation_results(self, info):
        return SimulationResult.objects.all()

    def resolve_simulation_result_by_id(self, info, simID):
        objects: QuerySet = SimulationResult.objects.filter(simID=simID)
        if objects.count() == 0:
            return None
        return objects[0]
