# Generated by Django 4.2.6 on 2023-10-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icedreamapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]