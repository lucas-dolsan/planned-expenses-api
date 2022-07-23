from rest_framework import viewsets, mixins

from api.controller import user_get_all
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin):
    queryset = user_get_all()
    serializer_class = UserSerializer
