# Generated by Django 2.2.7 on 2019-11-27 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0011_mainsitesettings_og_default_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainsitesettings',
            name='og_default_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='mainsitesettings',
            name='og_description',
            field=models.CharField(blank=True, default='The High End Fashion Retailer', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mainsitesettings',
            name='og_title',
            field=models.CharField(blank=True, default='ILLIYEEN', max_length=100, null=True),
        ),
    ]