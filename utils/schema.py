import graphene
from graphene_django.types import ObjectType

class MyObjectType(ObjectType):
    model = None
    model_type = None
    object = None
    objects = None

    def __init__(self, *args, **kwargs):
        self.object = graphene.Field(self.model_type, id=graphene.Int())
        self.objects = graphene.List(self.model_type)
        super(MyObjectType, self).__init__( *args, **kwargs)

    def resolve_object(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return self.model.objects.get(pk=id)
        return None
