# Generated by Django 3.1.6 on 2021-02-09 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20210209_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='age',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]