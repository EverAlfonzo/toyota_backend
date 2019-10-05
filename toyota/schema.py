import graphene
from django.contrib.auth import get_user_model
from graphql_jwt import ObtainJSONWebToken

from articles.schema import ArticlesQuery
from company.schema import CompanyQuery
from contacts.schema import ContactMutation
from location.schema import LocationQuery
from talleres.schema import TallerQuery, TallerMutation
from usuarios.schema import UsuariosMutation, UsuariosQuery
import graphql_jwt


class Query(TallerQuery, UsuariosQuery, ArticlesQuery,CompanyQuery, LocationQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class MyObtainJSONWebToken(ObtainJSONWebToken):
    """Obtain JSON Web Token mutation"""

    @classmethod
    def Field(cls, *args, **kwargs):
        cls._meta.arguments.update({
            get_user_model().USERNAME_FIELD: graphene.String(required=True),
            'password': graphene.String(required=True),
        })
        return super(MyObtainJSONWebToken, cls).Field(*args, **kwargs)

class Mutation(ContactMutation, UsuariosMutation, TallerMutation,graphene.ObjectType):
    token_auth = MyObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

# schema = graphene.Schema(query=Query,mutation=Mutation)

schema = graphene.Schema(query=Query,mutation=Mutation )