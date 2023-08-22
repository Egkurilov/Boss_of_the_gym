# Generated by Django 4.1.3 on 2022-11-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0005_alter_user_age_alter_user_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]