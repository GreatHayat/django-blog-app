# Generated by Django 2.2.5 on 2019-09-18 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crudApp', '0010_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_msg', models.TextField()),
                ('reply_date', models.DateTimeField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_comment', to='crudApp.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
