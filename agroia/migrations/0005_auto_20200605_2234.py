# Generated by Django 3.0.3 on 2020-06-06 03:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('agroia', '0004_auto_20200605_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_upload',
            field=models.DateField(default=datetime.datetime(2020, 6, 6, 3, 34, 38, 940779, tzinfo=utc)),
        ),
    ]
