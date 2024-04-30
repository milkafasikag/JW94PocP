# Generated by Django 4.2.4 on 2024-01-26 16:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_remove_payment_bank_recipt_bank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='transaction_reference',
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
