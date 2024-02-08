# Generated by Django 5.0 on 2024-02-06 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_video_alter_njoftime_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='njoftime',
            name='Data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 6, 21, 53, 56, 937837)),
        ),
        migrations.AlterField(
            model_name='njoftime',
            name='Teksti',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='pytje',
            name='Pytja',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='video',
            name='Data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 6, 21, 53, 56, 937837)),
        ),
    ]
