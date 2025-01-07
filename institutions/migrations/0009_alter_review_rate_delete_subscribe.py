# Generated by Django 5.1.2 on 2024-12-03 23:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0008_alter_institution_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.DeleteModel(
            name='Subscribe',
        ),
    ]
