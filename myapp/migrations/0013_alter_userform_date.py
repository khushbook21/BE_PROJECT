# Generated by Django 3.2.6 on 2022-05-05 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_userform_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 22, 13, 18, 649992)),
        ),
    ]
