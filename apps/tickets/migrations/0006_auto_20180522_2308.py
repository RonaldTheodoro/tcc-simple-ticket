# Generated by Django 2.0.5 on 2018-05-23 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='tickets',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
