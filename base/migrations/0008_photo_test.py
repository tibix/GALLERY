# Generated by Django 4.2.4 on 2023-11-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_photo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='test',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
