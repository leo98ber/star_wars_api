# Generated by Django 4.1.2 on 2022-11-03 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='deleted_date',
        ),
        migrations.RemoveField(
            model_name='character',
            name='modified_date',
        ),
    ]
