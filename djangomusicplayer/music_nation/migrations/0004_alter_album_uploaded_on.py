# Generated by Django 3.2.6 on 2021-08-21 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0003_alter_album_uploaded_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2021, 8, 21, 13, 37, 10, 290476)),
        ),
    ]
