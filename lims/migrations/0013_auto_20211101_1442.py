# Generated by Django 3.1.2 on 2021-11-01 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims', '0012_auto_20211101_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='left_padding',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='label',
            name='top_padding',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
