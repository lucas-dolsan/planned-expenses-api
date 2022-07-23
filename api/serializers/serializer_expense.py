from rest_framework import serializers

from api.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'user', 'name', 'expense_type', 'next_occurrence', 'periodicity_occurrence',
                  'include_current_month', 'value', 'observations')
