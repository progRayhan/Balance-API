# Generated by Django 4.1.1 on 2022-09-17 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taka', '0004_remove_balances_username_balances_account_holder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balances',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='taka.bank'),
        ),
    ]