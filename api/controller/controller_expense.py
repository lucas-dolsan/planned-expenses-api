from api.models import Expense


def expense_get_all():
    return Expense.objects.all()
