# Generated by Django 5.1.2 on 2024-12-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='title',
            field=models.CharField(default='Some title', max_length=200),
        ),
    ]
