# Generated by Django 3.2.6 on 2022-04-21 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_userform_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 22, 7, 26, 172525)),
        ),
    ]