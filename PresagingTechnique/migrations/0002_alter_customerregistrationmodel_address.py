# Generated by Django 4.1.3 on 2023-09-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PresagingTechnique", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerregistrationmodel",
            name="address",
            field=models.CharField(max_length=1000),
        ),
    ]
