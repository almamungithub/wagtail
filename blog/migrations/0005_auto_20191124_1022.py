# Generated by Django 2.2.7 on 2019-11-24 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogauthorsorderable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogdetailpage',
            old_name='blog_image',
            new_name='banner_image',
        ),
    ]
