# Generated by Django 4.1.1 on 2022-09-17 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taka', '0005_alter_balances_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balances',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banklist', to='taka.bank'),
        ),
    ]
