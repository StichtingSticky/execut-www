# Generated by Django 3.0.6 on 2020-09-09 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200909_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='speakers',
            field=models.ManyToManyField(blank=True, related_name='activities', to='core.Speaker', verbose_name='sprekers'),
        ),
    ]
