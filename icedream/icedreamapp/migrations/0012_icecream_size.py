# Generated by Django 4.2.6 on 2023-10-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icedreamapp', '0011_delete_conebox_alter_icecream_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='size',
            field=models.CharField(default=100, max_length=50),
            preserve_default=False,
        ),
    ]
