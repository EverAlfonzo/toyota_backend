from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from graphql import GraphQLError

import graphene
from graphene_django import DjangoObjectType

from usuarios.models import Profile
from utils.views import resize


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile

    def resolve_image(self, info, **kwargs):
        if not self.image:
            self.image = 'images/profiles/default.png'
        path = resize(str(self.image), '300,300')
        return path and info.context.build_absolute_uri(path) or None

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()



class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        name = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)

    def mutate(self, info, name, password, email, phone):
        if User.objects.filter(email=email).exists():
            raise GraphQLError('Este email ya se encuentra registrado')

        user = get_user_model()(
            first_name=name,
            username=email,
            email=email,
        )
        user.set_password(password)
        user.save()

        profile = Profile(user=user, phone=phone)
        profile.save()

        return CreateUser(user=user)


class UserData(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)

    def mutate(self, info, username):
        return CreateUser(user=User.objects.get(username=username))



class UsuariosMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    user_data = UserData.Field()

class UsuariosQuery(graphene.ObjectType):
    users = graphene.List(UserType)
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication Failure!')
        return user

    def resolve_users(self, info):
        return get_user_model().objects.all()