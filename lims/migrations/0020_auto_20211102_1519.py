# Generated by Django 3.1.2 on 2021-11-02 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims', '0019_auto_20211102_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testresult',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='testresult',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='testresult',
            name='researcher',
            field=models.ManyToManyField(blank=True, to='lims.Researcher'),
        ),
        migrations.AlterField(
            model_name='event',
            name='researcher',
            field=models.ManyToManyField(blank=True, to='lims.Researcher'),
        ),
    ]
