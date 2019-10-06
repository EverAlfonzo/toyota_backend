from datetime import datetime
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


class CreateService(graphene.Mutation):
    service = graphene.Field(ServiceType)

    class Arguments:
        user_id = graphene.ID(required=True)
        document = graphene.String(required=True)
        brand_id = graphene.ID(required=True)
        model_id = graphene.ID(required=True)
        year = graphene.Int(required=True)
        car_km = graphene.Int(required=True)
        license_plate = graphene.String(required=True)
        id_type = graphene.String(required=True)
        workshop_id = graphene.ID(required=True)
        comment = graphene.String(required=True)
        date = graphene.String(required=True)
        time = graphene.String(required=True)


    def mutate(self, info, user_id, document, brand_id, model_id, year, car_km,
               license_plate, id_type, workshop_id, date, time, comment):

        service = Service(
            user_id=user_id,
            document=document,
            brand_id=brand_id,
            model_id=model_id,
            year=year,
            car_km=car_km,
            license_plate=license_plate,
            id_type=id_type,
            workshop_id=workshop_id,
            comment=comment,
            date=datetime.strptime(date, "%Y-%m-%d"),
            time=datetime.strptime(time+":00", '%H:%M:%S').time()
        )
        service.save()
        return CreateService(service=service)


class TallerMutation(ObjectType):
    search_talleres = SearchTallerMutation.Field()
    create_service = CreateService.Field()
