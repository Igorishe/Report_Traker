from django.contrib import admin

from .models import Report, MobinetReport, MoneyBack


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('text', 'date', 'author', 'status', 'tag')
    search_fields = ('status', 'tag', 'author', 'date')
    list_filter = ('author', 'date', 'status', 'tag')


@admin.register(MobinetReport)
class MobinetReportAdmin(ReportAdmin):
    pass


@admin.register(MoneyBack)
class MoneyBackAdmin(admin.ModelAdmin):
    list_display = (
        'text', 'value', 'wallet', 'date', 'author', 'status', 'tag', 'link'
    )
    search_fields = ('status', 'tag', 'author', 'date', 'link')
    list_filter = ('author', 'date', 'status', 'tag', 'value')
