# Generated by Django 2.2.7 on 2019-11-19 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayCenters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_name', models.CharField(help_text='Center Name', max_length=100)),
                ('center_address', models.TextField(help_text='Address')),
                ('center_business_hours', models.TextField(help_text='Business Hours')),
                ('center_contact_no', models.CharField(help_text='Contact No', max_length=100)),
            ],
            options={
                'verbose_name': 'Display Center',
                'verbose_name_plural': 'Display Centers',
            },
        ),
    ]