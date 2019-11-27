#site_settings/models.py


from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, TabbedInterface, ObjectList
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting


@register_setting
class MainSiteSettings(BaseSetting):
    """Main site settings for our custom website."""

    title = models.CharField(max_length=100, blank=False, null=True, default="The High End Fashion Retailer | ILLIYEEN")
    og_title = models.CharField(max_length=100, blank=True, null=True, default="ILLIYEEN")
    og_description = models.CharField(max_length=100, blank=True, null=True, default="The High End Fashion Retailer")

    og_default_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    page_title_cart = models.CharField(max_length=100, blank=False, null=True, default="Shopping Bag | ILLIYEEN")
    page_title_checkout = models.CharField(max_length=100, blank=False, null=True, default="The High End Fashion Retailer | ILLIYEEN")
    page_title_payment = models.CharField(max_length=100, blank=False, null=True, default="Payment Confirmation | ILLIYEEN")
    page_title_search_result = models.CharField(max_length=100, blank=False, null=True, default="Search result | ILLIYEEN")

    page_title_profile = models.CharField(max_length=100, blank=False, null=True, default="Profile | ILLIYEEN")
    page_title_edit_profile = models.CharField(max_length=100, blank=False, null=True, default="Update Profile | ILLIYEEN")
    page_title_update_password = models.CharField(max_length=100, blank=False, null=True, default="Forgot password | ILLIYEEN")

    page_title_sign_in = models.CharField(max_length=100, blank=False, null=True, default="Sign In | ILLIYEEN")
    page_title_sign_up = models.CharField(max_length=100, blank=False, null=True, default="Sign Up | ILLIYEEN")

    page_title_success = models.CharField(max_length=100, blank=False, null=True, default="Order Confirmation | ILLIYEEN")
    page_title_cancel = models.CharField(max_length=100, blank=False, null=True, default="Order Cancellation | ILLIYEEN")
    page_title_error = models.CharField(max_length=100, blank=False, null=True, default="Order Error | ILLIYEEN")

    """Social media settings for our custom website."""
    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel URL")

    analytics = models.TextField( blank=True, null=True, help_text="Analytics")



    site_title_panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("og_title"),
            FieldPanel("og_description"),
            ImageChooserPanel("og_default_image"),
        ], heading="Site Title")
    ]

    page_title_panels = [
        MultiFieldPanel([
            FieldPanel("page_title_cart"),
            FieldPanel("page_title_checkout"),
            FieldPanel("page_title_payment"),
            FieldPanel("page_title_search_result"),

            FieldPanel("page_title_profile"),
            FieldPanel("page_title_edit_profile"),
            FieldPanel("page_title_update_password"),

            FieldPanel("page_title_sign_in"),
            FieldPanel("page_title_sign_up"),

            FieldPanel("page_title_success"),
            FieldPanel("page_title_cancel"),
            FieldPanel("page_title_error"),
        ], heading="Page Title")
    ]

    social_media_panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("instagram"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),

        ], heading="Social Media Link")
    ]

    analytics_panels = [
        MultiFieldPanel([
            FieldPanel("analytics"),


        ], heading="Analytics Code")
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(site_title_panels, heading='Site Title Settings'),
            ObjectList(page_title_panels, heading='Page Title Settings'),
            ObjectList(social_media_panels, heading='Social Media Settings'),
            ObjectList(analytics_panels, heading='Analytics Settings'),
        ]
    )

    class Meta:  # noqa
        verbose_name = "Site Info"
        verbose_name_plural = "All Site Info"



@register_setting(icon='mail')
class SmsCredSettings(BaseSetting):
    """sms Credential settings for our illiyeen website."""

    dev_url = models.URLField(blank=True, null=True, help_text="SMS DEV URL")
    dev_username = models.CharField(max_length=100, blank=False, null=True)
    dev_password = models.CharField(max_length=100, blank=False, null=True)
    dev_application_id = models.CharField(max_length=100, blank=False, null=True)
    dev_message_id = models.CharField(max_length=100, blank=False, null=True)
    dev_authorization = models.CharField(max_length=100, blank=False, null=True)
    dev_sms_from = models.CharField(max_length=100, blank=False, null=True)

    live_url = models.URLField(blank=True, null=True, help_text="SMS LIVE URL")
    live_username = models.CharField(max_length=100, blank=False, null=True)
    live_password = models.CharField(max_length=100, blank=False, null=True)
    live_application_id = models.CharField(max_length=100, blank=False, null=True)
    live_message_id = models.CharField(max_length=100, blank=False, null=True)
    live_authorization = models.CharField(max_length=100, blank=False, null=True)
    live_sms_from = models.CharField(max_length=100, blank=False, null=True)

    ACTIVE_SMS_CHOICES = (
        ('dev', 'DEV'),
        ('live', 'Live'),
    )
    active_sms = models.CharField(max_length=10, choices=ACTIVE_SMS_CHOICES)

    dev_panels = [
        MultiFieldPanel([
            FieldPanel("dev_url"),
            FieldPanel("dev_username"),
            FieldPanel("dev_password"),
            FieldPanel("dev_application_id"),
            FieldPanel("dev_message_id"),
            FieldPanel("dev_authorization"),
            FieldPanel("dev_sms_from"),
        ], heading="Sms Dev Settings")
    ]

    live_panels = [
        MultiFieldPanel([
            FieldPanel("live_url"),
            FieldPanel("live_username"),
            FieldPanel("live_password"),
            FieldPanel("live_application_id"),
            FieldPanel("live_message_id"),
            FieldPanel("live_authorization"),
            FieldPanel("live_sms_from"),
        ], heading="Sms Live Settings")
    ]

    settings_panels = [
        MultiFieldPanel([
            FieldPanel("active_sms"),

        ], heading="Sms Active Settings")
    ]



    edit_handler = TabbedInterface(
        [
            ObjectList(dev_panels, heading='Sms DEV Settings'),
            ObjectList(live_panels, heading='SMS Live Settings'),
            ObjectList(settings_panels, heading='Active Settings'),
        ]
    )

    class Meta:  # noqa
        verbose_name = "SMS Credential"
        verbose_name_plural = "All SMS Credential"


@register_setting(icon='form')
class ApiCredentialSettings(BaseSetting):
    """API Credential settings for our illiyeen website."""

    dev_url = models.URLField(blank=True, null=True, help_text="API DEV URL")
    dev_report_url = models.URLField(blank=True, null=True, help_text="API DEV REPORT URL")
    dev_consumer_key = models.CharField(max_length=100, blank=False, null=True)
    dev_consumer_secret = models.CharField(max_length=100, blank=False, null=True)
    dev_oauth_token = models.CharField(max_length=100, blank=False, null=True)
    dev_oauth_token_secret = models.CharField(max_length=100, blank=False, null=True)

    live_url = models.URLField(blank=True, null=True, help_text="SMS DEV URL")
    live_report_url = models.URLField(blank=True, null=True, help_text="SMS DEV URL")
    live_consumer_key = models.CharField(max_length=100, blank=False, null=True)
    live_consumer_secret = models.CharField(max_length=100, blank=False, null=True)
    live_oauth_token = models.CharField(max_length=100, blank=False, null=True)
    live_oauth_token_secret = models.CharField(max_length=100, blank=False, null=True)

    ACTIVE_API_CHOICES = (
        ('dev', 'DEV'),
        ('live', 'Live'),
    )
    active_api = models.CharField(max_length=10, null=True, choices=ACTIVE_API_CHOICES)




    dev_panels = [
        MultiFieldPanel([
            FieldPanel("dev_url"),
            FieldPanel("dev_report_url"),
            FieldPanel("dev_consumer_key"),
            FieldPanel("dev_consumer_secret"),
            FieldPanel("dev_oauth_token"),
            FieldPanel("dev_oauth_token_secret"),
        ], heading="API Dev Settings")
    ]

    live_panels = [
        MultiFieldPanel([
            FieldPanel("live_url"),
            FieldPanel("live_report_url"),
            FieldPanel("live_consumer_key"),
            FieldPanel("live_consumer_secret"),
            FieldPanel("live_oauth_token"),
            FieldPanel("live_oauth_token_secret"),
        ], heading="API Live Settings")
    ]

    settings_panels = [
        MultiFieldPanel([
            FieldPanel("active_api"),

        ], heading="Active API Settings")
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(dev_panels, heading='API DEV Settings'),
            ObjectList(live_panels, heading='API Live Settings'),
            ObjectList(settings_panels, heading='API Active Settings'),
        ]
    )

    class Meta:  # noqa
        verbose_name = "API Credential"
        verbose_name_plural = "All API Credential"
