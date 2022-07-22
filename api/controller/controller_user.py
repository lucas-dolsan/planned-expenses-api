from rest_framework import serializers

from api.models import User


def user_get_all():
    return User.objects.all()


def user_save(userSerializer):
    instance = User.objects.filter(email__exact=userSerializer.validated_data['email'])

    if instance is not None:
        instance = User(email=userSerializer.validated_data['email'],
                        username=userSerializer.validated_data['username'],
                        is_staff=False,
                        is_superuser=False)

    password = userSerializer.validated_data['password']
    password_confirm = userSerializer.validated_data['password_confirm']

    if password != password_confirm:
        raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
    instance.set_password(password)
    instance.save()
    return instance
