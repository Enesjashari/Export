# Generated by Django 5.0 on 2023-12-17 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pytje',
            name='Ju_kam_Pergjigjur',
            field=models.BooleanField(blank=True),
        ),
    ]