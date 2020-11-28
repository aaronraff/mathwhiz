# Generated by Django 3.0.4 on 2020-11-28 22:22

import backend.challenges.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Challenge",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "join_code",
                    models.CharField(
                        default=backend.challenges.models.generate_uuid, max_length=512
                    ),
                ),
            ],
        ),
    ]
