from api.models import BankAccount


def bank_account_get_all():
    return BankAccount.objects.all()
