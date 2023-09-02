from django.contrib import admin
from .models import Consignment

class ConsignmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'status',
        'image_1',
    )

    ordering = ('date_submitted',)


admin.site.register(Consignment, ConsignmentAdmin)
