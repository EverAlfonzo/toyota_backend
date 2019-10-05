import graphene
from django.db.migrations.graph import Node
from graphene.types.inputobjecttype import InputObjectType
from graphene.types.objecttype import ObjectType
from graphene_django.types import DjangoObjectType
from contacts.models import Contact

# Create a GraphQL type for the actor model
class ContactType(DjangoObjectType):

    class Meta:
        model = Contact

# Create a Query type
class Query(ObjectType):
    contact = graphene.Field(ContactType)

    def resolve_contact(self, info, **kwargs):
        return Contact.objects.first()

class CreateContact(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        message = graphene.String(required=True)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, email,message):
        contact = Contact(
            email=email,
            message=message
        )
        contact.save()
        return CreateContact(ok=True)


class Mutation(ObjectType):
    create_contact = CreateContact.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)