# Generated by Django 3.1.7 on 2021-03-11 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210309_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tagline',
            field=models.CharField(default='2021 is year of the daddy', max_length=200),
            preserve_default=False,
        ),
    ]
