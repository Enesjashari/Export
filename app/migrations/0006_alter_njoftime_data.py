# Generated by Django 5.0 on 2023-12-19 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_njoftime_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='njoftime',
            name='Data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 19, 18, 10, 54, 994879)),
        ),
    ]
