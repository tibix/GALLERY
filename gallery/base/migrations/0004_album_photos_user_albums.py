# Generated by Django 4.2.4 on 2023-08-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_album_photo_user_delete_gallery_album_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='photos', to='base.photo'),
        ),
        migrations.AddField(
            model_name='user',
            name='albums',
            field=models.ManyToManyField(related_name='albums', to='base.album'),
        ),
    ]
