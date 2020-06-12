# Generated by Django 3.0.3 on 2020-06-12 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroia', '0010_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_result',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='txt_result',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='crops'),
        ),
        migrations.AlterField(
            model_name='method',
            name='file',
            field=models.FileField(null=True, upload_to='methods'),
        ),
    ]
