# Generated by Django 2.2.7 on 2019-11-26 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('site_settings', '0004_auto_20191126_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smscredsettings',
            name='live_url',
            field=models.URLField(blank=True, help_text='SMS LIVE URL', null=True),
        ),
        migrations.CreateModel(
            name='ApiCredentialSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_url', models.URLField(blank=True, help_text='SMS DEV URL', null=True)),
                ('dev_report_url', models.URLField(blank=True, help_text='SMS DEV URL', null=True)),
                ('dev_consumer_key', models.CharField(max_length=100, null=True)),
                ('dev_consumer_secret', models.CharField(max_length=100, null=True)),
                ('dev_oauth_token', models.CharField(max_length=100, null=True)),
                ('dev_oauth_token_secret', models.CharField(max_length=100, null=True)),
                ('live_url', models.URLField(blank=True, help_text='SMS DEV URL', null=True)),
                ('live_report_url', models.URLField(blank=True, help_text='SMS DEV URL', null=True)),
                ('live_consumer_key', models.CharField(max_length=100, null=True)),
                ('live_consumer_secret', models.CharField(max_length=100, null=True)),
                ('live_oauth_token', models.CharField(max_length=100, null=True)),
                ('live_oauth_token_secret', models.CharField(max_length=100, null=True)),
                ('gtag', models.CharField(max_length=100, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
