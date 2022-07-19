from django.core.validators import MinValueValidator
from django.db import models
from . import User, Periodicity, ExpenseType


class Expense(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.PROTECT,
                                verbose_name='Usuário')
    name = models.CharField(max_length=155,
                            verbose_name='Nome da despesa')
    expense_type = models.IntegerField(default=ExpenseType.EXPENSE,
                                       choices=ExpenseType.choices,
                                       verbose_name='Tipo de Despesa')
    next_occurrence = models.DateField(verbose_name='Data da próxima ocorrência')
    periodicity_occurrence = models.IntegerField(default=Periodicity.ANNUAL,
                                                 choices=Periodicity.choices,
                                                 verbose_name='Periodicidade')
    include_current_month = models.BooleanField(default=True,
                                                verbose_name='Inclúir mês atual no cálculo da recorrência')
    value = models.FloatField(validators=[MinValueValidator(0.0)],
                              verbose_name='Valor')
    observations = models.TextField(max_length=5000,
                                    verbose_name='Observações')

    class Meta:
        verbose_name = 'Despesa'

    def __str__(self):
        return "{}".format(self.name)
    