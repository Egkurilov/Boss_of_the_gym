# Generated by Django 4.1.3 on 2022-11-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
