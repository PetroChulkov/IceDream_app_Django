# Generated by Django 4.2.6 on 2023-10-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icedreamapp', '0010_alter_conebox_size'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConeBox',
        ),
        migrations.AlterField(
            model_name='icecream',
            name='type',
            field=models.CharField(choices=[('Ice Cream', 'Ice Cream'), ('Sorbet', 'Sorbet'), ('Vegan', 'Vegan'), ('Cone/Box', 'Cone/Box')], default='IceCream', max_length=32),
        ),
    ]
