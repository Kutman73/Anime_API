# Generated by Django 4.1.4 on 2023-01-25 08:48

import anime.fileschek
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animeepisode',
            name='anime_video',
            field=models.FileField(max_length=255, storage=anime.fileschek.OverWriteStorage(), upload_to=anime.fileschek.FileStorage.get_path_to_episode, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
        migrations.AlterField(
            model_name='animeepisode',
            name='episode_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='animeepisode',
            name='title_episode',
            field=models.CharField(max_length=255),
        ),
    ]