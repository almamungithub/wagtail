# Generated by Django 2.2.7 on 2019-11-19 06:13

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('display_centers', '0002_auto_20191119_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='displaycenters',
            name='center_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='displaycenters',
            name='center_address',
            field=wagtail.core.fields.RichTextField(help_text='Center Address', null=True),
        ),
        migrations.AlterField(
            model_name='displaycenters',
            name='center_business_hours',
            field=wagtail.core.fields.RichTextField(help_text='Center Business Hours', null=True),
        ),
    ]
