import graphene


class BaseMutation(graphene.Mutation):
    class Arguments:
        department_id = graphene.ID(required=False)
        city_id = graphene.ID(required=False)
        name = graphene.String(required=False)

    @staticmethod
    def mutate(cls, info, department_id=None, city_id=None, name=None):
        queryset = info.return_type.graphene_type.queryset
        queryset = queryset.exclude(city__isnull=True, city__department__isnull=True)

        if department_id:
            queryset = queryset.filter(city__department_id=department_id)
        if city_id:
            queryset = queryset.filter(city_id=city_id)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return info.return_type.graphene_type(object_list=queryset)
