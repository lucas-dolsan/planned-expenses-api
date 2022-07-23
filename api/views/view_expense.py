from rest_framework import viewsets

from api.controller import expense_get_all
from api.serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = expense_get_all()
    serializer_class = ExpenseSerializer
