# Generated by Django 4.1.3 on 2022-11-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0006_alter_user_age_alter_user_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]