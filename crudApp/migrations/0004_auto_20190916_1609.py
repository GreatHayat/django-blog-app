# Generated by Django 2.2.5 on 2019-09-16 16:09

import crudApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0003_auto_20190916_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(upload_to='feature_images/', validators=[crudApp.models.validate_file_size]),
        ),
    ]
