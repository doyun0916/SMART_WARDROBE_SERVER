# Generated by Django 3.1 on 2020-10-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=120),
        ),
    ]
