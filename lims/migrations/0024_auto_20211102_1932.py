# Generated by Django 3.1.2 on 2021-11-03 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lims', '0023_auto_20211102_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lims.sample'),
        ),
    ]