# Generated by Django 5.1 on 2024-08-15 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EducationModules",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.IntegerField(
                        db_index=True, unique=True, verbose_name="Номер модуля"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=30,
                        unique=True,
                        verbose_name="Название модуля",
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание модуля")),
            ],
            options={
                "verbose_name": "Модуль",
                "verbose_name_plural": "Модули",
                "ordering": ["number"],
            },
        ),
    ]
