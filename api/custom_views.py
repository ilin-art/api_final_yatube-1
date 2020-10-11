from rest_framework import mixins, generics, viewsets


class CustomViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    pass
