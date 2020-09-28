import graphene

from simulatorAPI.queries import Query
from simulatorAPI.mutations import Mutation


schema = graphene.Schema(query=Query, mutation=Mutation)
