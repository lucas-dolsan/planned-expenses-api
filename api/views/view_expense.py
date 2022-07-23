from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.controller import expense_get_all
from api.serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    queryset = expense_get_all()
    serializer_class = ExpenseSerializer
