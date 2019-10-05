from xml.dom.minicompat import StringTypes

import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from company.models import CompanyImage
from xionict.views import resize
from .models import Company

class CompanyImageType(DjangoObjectType):
    class Meta:
        model = CompanyImage
    def resolve_image(self, info, **kwargs):
        path = resize(str(self.image), '600,600')
        return path and info.context.build_absolute_uri(path) or None

# Create a GraphQL type for the actor model
class CompanyType(DjangoObjectType):
    images = graphene.List(graphene.String)
    images_qty = graphene.Int()


    def resolve_image(self, info, **kwargs):
        path = resize(str(self.image), '600,600')
        return path and info.context.build_absolute_uri(path) or None

    def resolve_images(self, info, **kwargs):
        images = []
        for rel in self.companyimage_set.all():
            path = resize(str(rel.image), '600,600')
            images.append(path and info.context.build_absolute_uri(path) or None)
        return images

    def resolve_images_qty(self,info,**kwargs):
        return int(self.companyimage_set.all().count())



    class Meta:
        model = Company


# Create a Query type
class Query(ObjectType):
    company = graphene.Field(CompanyType)


    def resolve_company(self, info, **kwargs):
        return Company.objects.first()





schema = graphene.Schema(query=Query)