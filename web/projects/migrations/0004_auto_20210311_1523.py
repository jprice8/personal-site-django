# Generated by Django 3.1.7 on 2021-03-11 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210309_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='additional_notes',
            field=models.TextField(default='Daddys content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='Daddys description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='stack',
            field=models.TextField(default='Daddys stack'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='wish_list',
            field=models.TextField(default='Daddys gonzo'),
            preserve_default=False,
        ),
    ]
