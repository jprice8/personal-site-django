# Generated by Django 3.1.7 on 2021-03-12 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20210311_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tagline',
            field=models.CharField(default='One sentence tagline', max_length=80),
            preserve_default=False,
        ),
    ]
