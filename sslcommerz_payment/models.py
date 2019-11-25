from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, TabbedInterface, ObjectList
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting


@register_setting()
class SslcommerzCredential(BaseSetting):
    live_base_url = models.CharField(max_length=255, default="https://securepay.sslcommerz.com")
    sandbox_base_url = models.CharField(max_length=255, default="https://sandbox.sslcommerz.com")

    live_store_name = models.CharField(max_length=150, blank=True)
    live_store_id = models.CharField(max_length=150, blank=True)
    live_store_pass = models.CharField(max_length=150, blank=True)

    sandbox_store_name = models.CharField(max_length=150, blank=True)
    sandbox_store_id = models.CharField(max_length=150, blank=True)
    sandbox_store_pass = models.CharField(max_length=150, blank=True)

    success_url = models.CharField(max_length=255, blank=True)
    fail_url = models.CharField(max_length=255, blank=True)
    ipn_url = models.CharField(max_length=255, blank=True)
    cancel_url = models.CharField(max_length=255, blank=True)




    ACTIVE_PAYMENT_CHOICES = (
        ('sandbox', 'Sandbox'),
        ('live', 'Live'),
    )
    active_payment = models.CharField(max_length=10, choices=ACTIVE_PAYMENT_CHOICES)

    content_sandbox_panels =  [
        FieldPanel("sandbox_base_url"),
        FieldPanel("sandbox_store_name"),
        FieldPanel("sandbox_store_id"),
        FieldPanel("sandbox_store_pass"),
    ]

    content_live_panels = [
        FieldPanel("live_base_url"),
        FieldPanel("live_store_name"),
        FieldPanel("live_store_id"),
        FieldPanel("sandbox_store_pass"),
    ]

    settings_panels = [
        FieldPanel("success_url"),
        FieldPanel("fail_url"),
        FieldPanel("ipn_url"),
        FieldPanel("active_payment"),
    ]

    # This is where all the tabs are created
    edit_handler = TabbedInterface(
        [
            ObjectList(content_sandbox_panels, heading='Sandbox'),
            ObjectList(content_live_panels, heading='Live'),
            ObjectList(settings_panels, heading='Settings'),
        ]
    )

    class Meta:  # noqa

        verbose_name = "SSLCommerz Setting"
        verbose_name_plural = "SSLCommerz Settings"


class SslcommerzInformation(models.Model):
    transaction_id = models.CharField(max_length=100)
    order_id = models.IntegerField(default=0)
    order_detail = models.TextField(default='')
    date_time = models.DateTimeField(auto_now_add=True)
    gw_api_status = models.CharField(max_length=100)
    hash_verified_status = models.CharField(max_length=10)
    order_valid_api_status = models.CharField(max_length=100)
    risk_level = models.IntegerField()
    risk_title = models.CharField(max_length=255, default='')
    card_type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    currency = models.CharField(max_length=10)
    gw_api_response = models.TextField()
    order_valid_api_response = models.TextField()

    def __str__(self):
        return self.transaction_id

    class Meta:  # noqa

        verbose_name = "SSLCommerz Informations"
        verbose_name_plural = "SSLCommerz Informations"
