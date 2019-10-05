import graphene

from articles.schema import ArticlesQuery
from company.schema import CompanyQuery
from contacts.schema import ContactMutation
from location.schema import LocationQuery
from talleres.schema import TallerQuery, TallerMutation

class Query(TallerQuery,ArticlesQuery,CompanyQuery, LocationQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(ContactMutation, graphene.ObjectType):
    pass

# schema = graphene.Schema(query=Query,mutation=Mutation)

schema = graphene.Schema(query=Query,mutation=Mutation )