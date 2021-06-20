from django.contrib import admin

from . import models


class CustomerModelAdmin(admin.ModelAdmin):
    """ModelAdmin configuration class for Customer"""
    list_display = ('get_full_name', 'dob', )

    def get_full_name(self, obj):
        """Returns full name of the customer"""
        return f'{obj.first_name} {obj.last_name}'
    get_full_name.__name__ = 'Full Name'


class PolicyModelAdmin(admin.ModelAdmin):
    """ModelAdmin configuration class for Policy"""
    list_display = ('customer', 'type', 'premium', 'cover', 'state', 'start_date', 'end_date')


admin.site.register(models.Customer, CustomerModelAdmin)
admin.site.register(models.Policy, PolicyModelAdmin)
