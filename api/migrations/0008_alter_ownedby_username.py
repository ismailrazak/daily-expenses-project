# Generated by Django 5.1.2 on 2024-10-22 08:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_alter_ownedby_expense"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ownedby",
            name="username",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owes_to",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
