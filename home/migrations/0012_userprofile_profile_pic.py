# Generated by Django 3.1.2 on 2020-11-22 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20201123_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]