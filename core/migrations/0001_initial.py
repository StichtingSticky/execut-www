# Generated by Django 3.0.6 on 2020-09-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('domain', models.CharField(max_length=300)),
                ('google_tag_manager_id', models.CharField(max_length=300, verbose_name='google tag manager-id')),
                ('logo', models.FileField(blank=True, null=True, upload_to='site_logos/', verbose_name='logo')),
                ('custom_css', models.FileField(blank=True, null=True, upload_to='custom_css/', verbose_name='custom-css')),
                ('description', models.CharField(max_length=300)),
                ('keywords', models.CharField(max_length=500)),
            ],
        ),
    ]