# Generated by Django 5.1.2 on 2024-12-01 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0004_alter_review_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='rating',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=50),
        ),
    ]
