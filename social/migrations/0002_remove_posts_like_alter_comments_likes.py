# Generated by Django 4.1.2 on 2022-11-21 04:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='like',
        ),
        migrations.AlterField(
            model_name='comments',
            name='likes',
            field=models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]