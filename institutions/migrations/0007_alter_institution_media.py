# Generated by Django 5.1.2 on 2024-12-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0006_institution_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='ins_media/'),
        ),
    ]
