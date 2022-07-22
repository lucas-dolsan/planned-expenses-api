from rest_framework import serializers

from api.controller import user_save
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     required=True)
    password_confirm = serializers.CharField(write_only=True,
                                             required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password_confirm', 'email', 'name', 'profile_image')
        extra_kwargs = {'password': {'write_only': True}}
        extra_kwargs = {'password_confirm': {'write_only': True}}

    def save(self):
        user_save(self)
