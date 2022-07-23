from rest_framework import serializers

from api.models import BankAccount


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('id', 'bank', 'name', 'opening_balance', 'current_balance')
