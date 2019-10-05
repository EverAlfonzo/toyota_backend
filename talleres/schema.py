from random import randint

import graphene
from django.db.models.aggregates import Count
from graphene_django.types import DjangoObjectType, ObjectType

from toyota.settings import MEDIA_URL
from utils.mutations import BaseMutation
from utils.views import resize
from .models import Taller
from graphene_django.converter import convert_django_field, convert_field_to_string
# from geoposition.fields import GeopositionField

# @convert_django_field.register(GeopositionField)
# def convert_geofield_to_string(field, registry=None):
#      return graphene.String(description=field.help_text, required=not field.null)

class TallerType(DjangoObjectType):

    def resolve_image(self, info, **kwargs):
        if not self.image:
            self.image = 'images/talleres/default.png'
        path = resize(str(self.image),'300,300')
        return path and info.context.build_absolute_uri(path) or None


    class Meta:
        model = Taller

class TallerQuery(ObjectType):
    taller = graphene.Field(TallerType, id=graphene.Int())
    talleres = graphene.List(TallerType)

    def resolve_taller(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Taller.objects.get(pk=id)
        return None

    def resolve_talleres(self, info, **kwargs):
        return Taller.objects.all()



class SearchTallerMutation(BaseMutation):
    object_list = graphene.List(TallerType)
    queryset = Taller.objects.all()




class TallerMutation(ObjectType):
    search_talleres = SearchTallerMutation.Field()
