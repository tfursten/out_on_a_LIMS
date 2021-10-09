# Generated by Django 3.1.2 on 2021-10-09 10:23

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('lims', '0002_auto_20211009_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True),
        ),
    ]