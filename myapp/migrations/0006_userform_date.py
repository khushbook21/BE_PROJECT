# Generated by Django 3.2.6 on 2022-04-21 05:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_userform_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userform',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 4, 21, 10, 54, 52, 362056)),
        ),
    ]
