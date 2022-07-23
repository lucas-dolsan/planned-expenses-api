from rest_framework import viewsets

from api.controller import bank_account_get_all
from api.serializers import BankAccountSerializer


class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = bank_account_get_all()
    serializer_class = BankAccountSerializer
