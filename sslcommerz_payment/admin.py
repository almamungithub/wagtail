from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from sslcommerz_payment.models import SslcommerzCredential


# class SslcommerzCredentialAdmin(ModelAdmin):
#     model = SslcommerzCredential
#     menu_label = 'SSLCommerz'  # ditch this to use verbose_name_plural from model
#     menu_icon = 'cog'  # change as required
#
#     fieldsets = [
#         ('Default Information', {'fields': ['active_payment', 'live_base_url', 'sandbox_base_url', 'success_url', 'fail_url', 'cancel_url']}),
#         ('For Live information', {'fields': ['live_store_name', 'live_store_id', 'live_store_pass']}),
#         ('For Sandbox information', {'fields': ['sandbox_store_name', 'sandbox_store_id', 'sandbox_store_pass']}),
#     ]
#
#     readonly_fields = ["live_base_url", "sandbox_base_url"]
#
#     def has_add_permission(self, request, obj=None):
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#     # def get_form(self, request, obj=None, change=False, **kwargs):
#     #     form = super(CredentialAdmin, self).get_form(request, obj, change, **kwargs)
#     #     print(form.base_fields['active_payment'].values())
#     #     return form
#
# modeladmin_register(SslcommerzCredentialAdmin)
# # admin.site.register(SslcommerzCredential, SslcommerzCredentialAdmin)
