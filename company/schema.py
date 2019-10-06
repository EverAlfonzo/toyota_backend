from xml.dom.minicompat import StringTypes

import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from company.models import CompanyImage, Brand, Model
from utils.views import resize
from .models import Company


class ModelType(DjangoObjectType):
    class Meta:
        model = Model

class BrandType(DjangoObjectType):

    def resolve_image(self, info, **kwargs):
        path = resize(str(self.image), '300,300')
        return path and info.context.build_absolute_uri(path) or None

    class Meta:
        model = Brand






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
class CompanyQuery(ObjectType):
    company = graphene.Field(CompanyType)
    brands = graphene.List(BrandType)
    brand = graphene.Field(BrandType, id=graphene.Int())

    models = graphene.List(ModelType)
    model = graphene.Field(ModelType, id=graphene.Int())

    def resolve_model(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Model.objects.get(pk=id)
        return None

    def resolve_models(self, info, **kwargs):
        return Model.objects.all()

    def resolve_brand(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Brand.objects.get(pk=id)
        return None

    def resolve_brands(self, info, **kwargs):
        return Brand.objects.all()

    def resolve_company(self, info, **kwargs):
        return Company.objects.first()


schema = graphene.Schema(query=CompanyQuery)