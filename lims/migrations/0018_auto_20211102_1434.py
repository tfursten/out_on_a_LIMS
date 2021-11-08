# Generated by Django 3.1.2 on 2021-11-02 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lims', '0017_auto_20211101_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('protocol', models.TextField(blank=True, null=True)),
                ('detects', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('result', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative'), ('Pending', 'Pending'), ('Unknown', 'Unknown'), ('Inconclusive', 'Inconclusive')], default='Pending', max_length=15)),
                ('notes', models.TextField(blank=True, null=True)),
                ('value', models.CharField(blank=True, max_length=100, null=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lims.test')),
            ],
        ),
        migrations.AddField(
            model_name='sample',
            name='results',
            field=models.ManyToManyField(blank=True, to='lims.TestResult'),
        ),
    ]