#site_settings/models.py
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting

@register_setting
class MainSiteSettings(BaseSetting):
    """Main site settings for our custom website."""

    site_name = models.CharField(max_length=100, blank=False, null=True)
    site_contact_name = models.CharField(max_length=100, blank=False, null=True)
    site_contact_no = models.CharField(max_length=100, blank=False, null=True)


    panels = [
        MultiFieldPanel([
            FieldPanel("site_name"),
            FieldPanel("site_contact_name"),
            FieldPanel("site_contact_no"),
        ], heading="Main Content Settings")
    ]

@register_setting
class SocialMediaSettings(BaseSetting):
    """Social media settings for our custom website."""

    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
        ], heading="Social Media Settings")
    ]
