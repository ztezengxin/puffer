# Generated by Django 2.0.5 on 2018-05-31 23:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tokenStorageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unassigned_tokens', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), size=None)),
            ],
        ),
    ]
