from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Nome')
    logo = models.ImageField(verbose_name='Logomarca')

    class Meta:
        verbose_name = 'Banco'

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    bank = models.ForeignKey(Bank,
                             on_delete=models.PROTECT,
                             verbose_name='Banco')
    name = models.CharField(max_length=255,
                            verbose_name='Nome')
    opening_balance = models.FloatField(verbose_name='Saldo Inicial')
    current_balance = models.FloatField(verbose_name='Saldo Atual')

    class Meta:
        verbose_name = 'Conta Bancária'
        verbose_name_plural = 'Contas Bancárias'

    def __str__(self):
        return self.name
