# Generated by Django 4.1.3 on 2022-11-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('type', models.CharField(default=None, max_length=255)),
                ('cost', models.CharField(default=None, max_length=255)),
            ],
        ),
    ]