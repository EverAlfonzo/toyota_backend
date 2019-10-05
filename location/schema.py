
from graphene import ObjectType
from graphene_django import DjangoObjectType
import graphene
from location.models import City, Department


class CityType(DjangoObjectType):
    class Meta:
        model = City

class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department

class LocationQuery(ObjectType):
    city = graphene.Field(CityType, id=graphene.Int())
    cities = graphene.List(CityType)
    department = graphene.Field(DepartmentType, id=graphene.Int())
    departments = graphene.List(DepartmentType)

    def resolve_city(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return City.objects.get(pk=id)
        return None

    def resolve_cities(self, info, **kwargs):
        return City.objects.all()

    def resolve_department(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Department.objects.get(pk=id)
        return None

    def resolve_departments(self, info, **kwargs):
        return Department.objects.all()

schema = graphene.Schema(query=LocationQuery)