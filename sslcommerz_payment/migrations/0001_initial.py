# Generated by Django 2.2.7 on 2019-11-24 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='SslcommerzInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=100)),
                ('order_id', models.IntegerField(default=0)),
                ('order_detail', models.TextField(default='')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('gw_api_status', models.CharField(max_length=100)),
                ('hash_verified_status', models.CharField(max_length=10)),
                ('order_valid_api_status', models.CharField(max_length=100)),
                ('risk_level', models.IntegerField()),
                ('risk_title', models.CharField(default='', max_length=255)),
                ('card_type', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('currency', models.CharField(max_length=10)),
                ('gw_api_response', models.TextField()),
                ('order_valid_api_response', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SslcommerzCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live_base_url', models.CharField(default='https://securepay.sslcommerz.com', max_length=255)),
                ('sandbox_base_url', models.CharField(default='https://sandbox.sslcommerz.com', max_length=255)),
                ('live_store_name', models.CharField(blank=True, max_length=150)),
                ('live_store_id', models.CharField(blank=True, max_length=150)),
                ('live_store_pass', models.CharField(blank=True, max_length=150)),
                ('sandbox_store_name', models.CharField(blank=True, max_length=150)),
                ('sandbox_store_id', models.CharField(blank=True, max_length=150)),
                ('sandbox_store_pass', models.CharField(blank=True, max_length=150)),
                ('success_url', models.CharField(blank=True, max_length=255)),
                ('fail_url', models.CharField(blank=True, max_length=255)),
                ('ipn_url', models.CharField(blank=True, max_length=255)),
                ('cancel_url', models.CharField(blank=True, max_length=255)),
                ('active_payment', models.CharField(choices=[('sandbox', 'Sandbox'), ('live', 'Live')], max_length=10)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),

            ],
            options={
                'verbose_name': 'SSLCommerz Setting',
                'verbose_name_plural': 'SSLCommerz Settings',
            },
        ),
    ]
