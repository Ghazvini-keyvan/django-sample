from django.contrib import admin
from .models import Customer,Usage
# Register your models here.
admin.site.register(Customer)

#admin.site.register(Usage)
@admin.register(Usage)
class UsageAdmin(admin.ModelAdmin):
    list_display = ('usage','date')
    list_filter = ('usage','date')
    