# Generated by Django 3.2.9 on 2022-07-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.URLField(blank=True, default=None, null=True, verbose_name='Imagem do perfil'),
        ),
    ]
