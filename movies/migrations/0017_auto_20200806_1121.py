# Generated by Django 3.0.8 on 2020-08-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_auto_20200806_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='user_avatars/1.jpg', null=True, upload_to='user_avatars/', verbose_name='Аватарка'),
        ),
    ]
