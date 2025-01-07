# Generated by Django 5.1.2 on 2024-12-18 11:50

import auth_system.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0011_alter_review_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='ins_media/', validators=[auth_system.validators.validate_image_size]),
        ),
    ]
