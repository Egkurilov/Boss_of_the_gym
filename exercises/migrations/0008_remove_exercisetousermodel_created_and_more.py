# Generated by Django 4.1.4 on 2023-08-10 21:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_exercisetousermodel_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisetousermodel',
            name='created',
        ),
        migrations.AddField(
            model_name='exerciseuserresult',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
