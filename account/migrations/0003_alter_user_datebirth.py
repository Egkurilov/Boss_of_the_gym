# Generated by Django 4.1.4 on 2023-03-08 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_age_user_datebirth_rename_bio_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='datebirth',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]