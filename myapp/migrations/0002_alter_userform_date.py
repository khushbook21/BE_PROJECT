# Generated by Django 3.2.6 on 2022-04-21 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='date',
            field=models.DateField(default='2022-04-11'),
        ),
    ]
