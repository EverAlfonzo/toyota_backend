import graphene

from talleres.schema import TallerQuery


class Query(TallerQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

# class Mutation(graphene.ObjectType):
#     pass

# schema = graphene.Schema(query=Query,mutation=Mutation)

schema = graphene.Schema(query=Query)