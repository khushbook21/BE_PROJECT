# Generated by Django 3.2.6 on 2022-04-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_userform_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='date',
            field=models.DateField(default=8),
        ),
    ]