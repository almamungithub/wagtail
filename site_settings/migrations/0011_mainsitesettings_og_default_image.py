# Generated by Django 2.2.7 on 2019-11-27 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('site_settings', '0010_auto_20191127_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainsitesettings',
            name='og_default_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
