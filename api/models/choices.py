from django.db import models


class Periodicity(models.IntegerChoices):
    MONTHLY = 1, 'Mensal'
    BIMONTHLY = 2, 'Bimestral'
    TRIMONTHLY = 3, 'Trimestral'
    BIANNUAL = 6, 'Semestral'
    ANNUAL = 12, 'Anual'


class ExpenseType(models.IntegerChoices):
    EXPENSE = 1, 'Despesa'
    GOAL = 2, 'Meta'


class TransactionType(models.IntegerChoices):
    DEBIT = 1, 'Débito'
    CREDIT = 2, 'Crédito'


class TransactionStatus(models.IntegerChoices):
    PENDING = 1, 'Pendente'
    PAID_OUT = 2, 'Quitado'
