# Generated by Django 4.2.3 on 2024-02-27 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posting_service", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="freelancer",
        ),
        migrations.DeleteModel(
            name="Freelancer",
        ),
    ]
