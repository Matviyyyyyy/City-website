# Generated by Django 5.1.2 on 2024-12-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walking', '0007_walk_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walk',
            name='goat',
            field=models.CharField(max_length=1000),
        ),
    ]
