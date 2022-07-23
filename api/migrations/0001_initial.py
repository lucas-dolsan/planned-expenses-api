# Generated by Django 3.2.9 on 2022-07-22 02:27

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=155, verbose_name='Usuário')),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(error_messages={'unique': 'O email cadastrado já existe.'}, max_length=155, unique=True)),
                ('name', models.CharField(max_length=155, verbose_name='Nome do usuário')),
                ('profile_image', models.URLField(default=None, verbose_name='Imagem do perfil')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Membro admin')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super usuário')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('logo', models.ImageField(upload_to='', verbose_name='Logomarca')),
            ],
            options={
                'verbose_name': 'Banco',
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('opening_balance', models.FloatField(verbose_name='Saldo Inicial')),
                ('current_balance', models.FloatField(verbose_name='Saldo Atual')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.bank', verbose_name='Banco')),
            ],
            options={
                'verbose_name': 'Conta Bancária',
                'verbose_name_plural': 'Contas Bancárias',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Nome')),
                ('expense_type', models.IntegerField(choices=[(1, 'Despesa'), (2, 'Meta')], default=1, verbose_name='Tipo de Despesa')),
                ('next_occurrence', models.DateField(verbose_name='Data da próxima ocorrência')),
                ('periodicity_occurrence', models.IntegerField(choices=[(1, 'Mensal'), (2, 'Bimestral'), (3, 'Trimestral'), (6, 'Semestral'), (12, 'Anual')], default=12, verbose_name='Periodicidade')),
                ('include_current_month', models.BooleanField(default=True, verbose_name='Inclúir mês atual no cálculo da recorrência')),
                ('value', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Valor')),
                ('observations', models.TextField(max_length=5000, verbose_name='Observações')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Despesa',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.IntegerField(choices=[(1, 'Débito'), (2, 'Crédito')], default=1, verbose_name='Tipo de transação')),
                ('creation_date_time', models.DateTimeField(auto_now=True, verbose_name='Data/hora criação')),
                ('payment_date', models.DateField(blank=True, default=None, null=True, verbose_name='Data pagamento')),
                ('value', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Valor')),
                ('status', models.IntegerField(choices=[(1, 'Pendente'), (2, 'Quitado')], default=1, verbose_name='status de transação')),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.bankaccount', verbose_name='Banco')),
                ('expanse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.expense', verbose_name='Despesa')),
            ],
            options={
                'verbose_name': 'Banco',
            },
        ),
    ]