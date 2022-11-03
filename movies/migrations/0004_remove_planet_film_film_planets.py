# Generated by Django 4.1.2 on 2022-11-03 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_film_company_producer_film_director_film_open_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planet',
            name='film',
        ),
        migrations.AddField(
            model_name='film',
            name='planets',
            field=models.ManyToManyField(to='movies.planet'),
        ),
    ]
