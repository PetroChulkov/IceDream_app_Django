# Generated by Django 4.2.6 on 2023-10-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icedreamapp', '0007_alter_cartitem_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='special',
            field=models.BooleanField(default=False),
        ),
    ]
