# Generated by Django 3.1.7 on 2021-03-10 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210309_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='additional_notes',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='stack',
        ),
        migrations.RemoveField(
            model_name='project',
            name='wish_list',
        ),
    ]
