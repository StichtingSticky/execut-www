# Generated by Django 3.0.6 on 2020-09-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200909_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='hero_button_enabled',
            field=models.BooleanField(default=False, verbose_name='schakel knop onder hero-tekst in'),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='hero_button_link',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='koppeling achter de knop onder de hero-tekst'),
        ),
    ]
