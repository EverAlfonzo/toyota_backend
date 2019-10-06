from random import randint

import graphene
from django.db.models.aggregates import Count
from graphene_django.types import DjangoObjectType, ObjectType

from talleres.models import Service
from toyota.settings import MEDIA_URL
from utils.mutations import BaseMutation
from utils.views import resize
from .models import Taller, Service, ServiceType as ServiceTypeModel

class TallerType(DjangoObjectType):

    def resolve_image(self, info, **kwargs):
        if not self.image:
            self.image = 'images/talleres/default.png'
        path = resize(str(self.image),'300,300')
        return path and info.context.build_absolute_uri(path) or None

    class Meta:
        model = Taller

class ServiceTypeModelType(DjangoObjectType):

    class Meta:
        model = ServiceTypeModel

class ServiceType(DjangoObjectType):

    class Meta:
        model = Service


class TallerQuery(ObjectType):
    taller = graphene.Field(TallerType, id=graphene.Int())
    talleres = graphene.List(TallerType)
    service_type = graphene.Field(ServiceTypeModelType, id=graphene.Int())
    services_types = graphene.List(ServiceTypeModelType)
    service = graphene.Field(ServiceType, id=graphene.Int())
    services = graphene.List(ServiceType)

    def resolve_taller(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Taller.objects.get(pk=id)
        return None

    def resolve_talleres(self, info, **kwargs):
        return Taller.objects.all()

    def resolve_service(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Service.objects.get(pk=id)
        return None

    def resolve_services(self, info, **kwargs):
        return Service.objects.all()

    def resolve_service_type(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return ServiceTypeModel.objects.get(pk=id)
        return None

    def resolve_services_types(self, info, **kwargs):
        return ServiceTypeModel.objects.all()


class SearchTallerMutation(BaseMutation):
    object_list = graphene.List(TallerType)
    queryset = Taller.objects.all()


class TallerMutation(ObjectType):
    search_talleres = SearchTallerMutation.Field()
