# Generated by Django 3.0.3 on 2020-06-12 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroia', '0011_auto_20200611_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='method',
            old_name='file',
            new_name='script',
        ),
        migrations.AddField(
            model_name='method',
            name='weights',
            field=models.FileField(null=True, upload_to='methods'),
        ),
    ]
