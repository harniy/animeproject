# Generated by Django 3.0.8 on 2020-08-03 16:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='favourite',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='favourite'),
        ),
    ]
