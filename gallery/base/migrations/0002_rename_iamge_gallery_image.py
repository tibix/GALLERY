# Generated by Django 4.2.4 on 2023-08-08 15:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="gallery",
            old_name="iamge",
            new_name="image",
        ),
    ]
