# Generated by Django 4.1.4 on 2023-03-19 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0005_alter_exercisetousermodel_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseuserresult',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.exerciselist'),
        ),
    ]
