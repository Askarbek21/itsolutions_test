from django.contrib import admin

from .models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'amount', 'status', 'type', 'category', 'comment']
    list_filter = ['status', 'type', 'category', 'subcategory', 'created_at']