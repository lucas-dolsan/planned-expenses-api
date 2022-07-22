from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework import routers

from api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', lambda req: redirect('/api/v1/')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
