from random import randint

import graphene
from django.db.models.aggregates import Count
from graphene_django.types import DjangoObjectType, ObjectType

from toyota.settings import MEDIA_URL
from utils.views import resize
from .models import Article

class ArticleType(DjangoObjectType):

    def resolve_image(self, info, **kwargs):
        if not self.image:
            self.image = 'images/default.png'
        path = resize(str(self.image),'300,300')
        return path and info.context.build_absolute_uri(path) or None


    class Meta:
        model = Article

class ArticlesQuery(ObjectType):
    article = graphene.Field(ArticleType, id=graphene.Int())
    articles = graphene.List(ArticleType)
    random_articles = graphene.List(ArticleType)

    def resolve_article(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Article.objects.get(pk=id)
        return None

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()



schema = graphene.Schema(query=ArticlesQuery)