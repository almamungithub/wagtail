from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import DisplayCentersDetailPage
from wagtail.contrib.modeladmin.mixins import ThumbnailMixin


class DisplayCentersAdmin(ThumbnailMixin, ModelAdmin):
    """Subscriber admin."""

    model = DisplayCentersDetailPage
    menu_label = "Display Centers"
    menu_icon = "list-ul"
    menu_order = 99999
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("center_name", "admin_thumb",  "center_contact_no", "center_address_full", "center_business_hours","google_map_location")
    search_fields = ("center_name", "center_address", "center_contact_no",)

    def center_address_full(self, obj):
        return obj.center_address

    center_address_full.short_description = 'Address'

    def google_map_location(self, obj):

        return format_html(
            '<a target="_blank" href="{}"> Show Map </span>',
            obj.google_map_link,

        )

    google_map_location.short_description = 'Location'



    thumb_image_field_name = 'center_image'
    thumb_image_filter_spec = 'fill-100x100'  # this is the default
    thumb_image_width = 100  # this is the default
    thumb_classname = 'admin-thumb'  # this is the default
    thumb_col_header_text = 'Picture'  # this is the default
    thumb_default = 'http://lorempixel.com/100/100'

modeladmin_register(DisplayCentersAdmin)
