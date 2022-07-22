from rest_framework import viewsets

from api.controller import user_get_all
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = user_get_all()
    serializer_class = UserSerializer
