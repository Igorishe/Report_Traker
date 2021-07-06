from django.contrib import admin

from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('text', 'date', 'author', 'status',)
    search_fields = ('status', 'author', 'date')
    list_filter = ('author', 'date', 'status')
