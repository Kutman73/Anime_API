# Generated by Django 4.1.4 on 2023-01-20 10:17

import anime.fileschek
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='number',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='number',
        ),
        migrations.RemoveField(
            model_name='statusanime',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='statusanime',
            name='number',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='number',
        ),
        migrations.RemoveField(
            model_name='voiceacting',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='voiceacting',
            name='number',
        ),
        migrations.AlterField(
            model_name='anime',
            name='cover_anime',
            field=models.ImageField(storage=anime.fileschek.OverWriteStorage(), upload_to=anime.fileschek.get_path_to_cover_anime, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png']), anime.fileschek.check_file_anime_cover_size]),
        ),
        migrations.AlterField(
            model_name='animeepisode',
            name='anime_video',
            field=models.FileField(storage=anime.fileschek.OverWriteStorage(), unique=True, upload_to=anime.fileschek.get_path_to_episode, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
        migrations.AlterField(
            model_name='animemovie',
            name='anime_movie_video',
            field=models.FileField(storage=anime.fileschek.OverWriteStorage(), unique=True, upload_to=anime.fileschek.get_path_to_movie, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]
