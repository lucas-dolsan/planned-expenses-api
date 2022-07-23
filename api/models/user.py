from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=155,
                                verbose_name='Usuário')
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=155,
                              unique=True,
                              error_messages=
                              {
                                  'unique': "O email cadastrado já existe."
                              })
    name = models.CharField(max_length=155,
                            verbose_name='Nome do usuário')
    profile_image = models.URLField(default=None,
                                    null=True,
                                    blank=True,
                                    verbose_name='Imagem do perfil')
    is_staff = models.BooleanField(default=False,
                                   verbose_name='Membro admin')
    is_superuser = models.BooleanField(default=False,
                                       verbose_name='Super usuário')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Usuário'

    def __str__(self):
        return "{}".format(self.email)
