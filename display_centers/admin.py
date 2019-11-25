from django.contrib import admin

# Register your models here.
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import DisplayCentersDetailPage


class DisplayCentersAdmin(ModelAdmin):
    """Subscriber admin."""

    model = DisplayCentersDetailPage
    menu_label = "Display Centers"
    menu_icon = "list-ul"
    menu_order = 99999
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("center_name", "center_address", "center_business_hours", "center_image", "center_contact_no",)
    search_fields = ("center_name", "center_address", "center_contact_no",)

modeladmin_register(DisplayCentersAdmin)
