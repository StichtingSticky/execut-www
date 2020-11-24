# Generated by Django 3.0.6 on 2020-09-09 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200909_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='committee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.Committee'),
            preserve_default=False,
        ),
    ]
