# Generated by Django 4.0.6 on 2022-07-28 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RoadmapItem",
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
                    "page",
                    models.TextField(
                        choices=[
                            ("Simplista", "Simplista"),
                            ("Roundista", "Roundista"),
                            ("Stylizta", "Stylizta"),
                        ]
                    ),
                ),
                ("block_name", models.TextField()),
                ("block_id", models.IntegerField()),
                ("alt_names", models.TextField(null=True)),
                ("thumbnail", models.ImageField(upload_to="")),
            ],
        ),
    ]