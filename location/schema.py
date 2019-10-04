from graphene_django import DjangoObjectType

from location.models import City, Department


class CityType(DjangoObjectType):
    class Meta:
        model = City

class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department
