# Generated by Django 4.1.2 on 2022-11-03 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_film_deleted_date_remove_film_modified_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='company_producer',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='film',
            name='open_text',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='film',
            name='productor',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='film',
            name='release_date',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('location', models.CharField(blank=True, max_length=150, null=True)),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.film')),
            ],
            options={
                'verbose_name': 'Modelo Base',
                'verbose_name_plural': 'Modelos Base',
                'abstract': False,
            },
        ),
    ]
