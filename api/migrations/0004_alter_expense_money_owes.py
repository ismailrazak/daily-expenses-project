# Generated by Django 5.1.2 on 2024-10-21 18:46

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_expense_money_owes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="money_owes",
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
