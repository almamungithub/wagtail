# Generated by Django 2.2.7 on 2019-11-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0009_mainsitesettings_analytics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainsitesettings',
            name='analytics',
            field=models.TextField(blank=True, help_text='Analytics', null=True),
        ),
    ]
