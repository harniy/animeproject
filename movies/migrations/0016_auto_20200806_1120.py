# Generated by Django 3.0.8 on 2020-08-06 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_auto_20200806_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_avatars/', verbose_name='Аватарка'),
        ),
    ]
