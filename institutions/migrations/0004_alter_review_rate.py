# Generated by Django 5.1.2 on 2024-12-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0003_remove_walk_events_remove_walk_institutions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(blank=True, default=50, null=True),
        ),
    ]
