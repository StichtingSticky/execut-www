# Generated by Django 3.0.6 on 2020-09-09 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200909_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='committee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.Committee', verbose_name='commissie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='is_organizational',
            field=models.BooleanField(default=False, verbose_name='is organisatorisch'),
        ),
    ]
