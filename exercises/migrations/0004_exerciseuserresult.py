# Generated by Django 4.1.4 on 2023-03-08 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0003_exerciselist_exercisetousermodel_exercisetype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseUserResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(default=None, max_length=255)),
                ('repeat', models.CharField(default=None, max_length=255)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.exercisetype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'exercise_result',
            },
        ),
    ]
