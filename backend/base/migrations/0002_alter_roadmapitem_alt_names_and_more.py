# Generated by Django 4.0.6 on 2022-07-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roadmapitem",
            name="alt_names",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="roadmapitem",
            name="block_name",
            field=models.CharField(max_length=100),
        ),
    ]
