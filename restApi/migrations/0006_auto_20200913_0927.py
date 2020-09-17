# Generated by Django 3.1 on 2020-09-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0005_account_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('email', models.EmailField(max_length=70, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='token',
        ),
    ]
