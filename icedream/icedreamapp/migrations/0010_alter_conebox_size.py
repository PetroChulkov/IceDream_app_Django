# Generated by Django 4.2.6 on 2023-10-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icedreamapp', '0009_conebox_icecream_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conebox',
            name='size',
            field=models.CharField(max_length=50),
        ),
    ]
