# Generated by Django 3.1.2 on 2021-10-27 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lims', '0003_auto_20211027_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lims.location'),
        ),
    ]
