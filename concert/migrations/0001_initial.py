# Generated by Django 4.1.1 on 2022-09-20 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Концерт',
                'verbose_name_plural': 'Концерты',
                'db_table': 'concert',
            },
        ),
    ]
