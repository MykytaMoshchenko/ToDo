# Generated by Django 4.1.7 on 2023-03-16 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("to_do", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["is_completed", "deadline"]},
        ),
    ]
