# Generated by Django 3.0.6 on 2021-03-15 10:00

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200909_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='long_description',
            field=tinymce.models.HTMLField(default='hallo', verbose_name='lange omschrijving'),
            preserve_default=False,
        ),
    ]
