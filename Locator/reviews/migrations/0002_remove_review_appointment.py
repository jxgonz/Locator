# Generated by Django 4.2.3 on 2024-03-01 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="appointment",
        ),
    ]