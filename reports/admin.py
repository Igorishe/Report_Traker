from django.contrib import admin

from .models import Report, MobinetReport


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('text', 'date', 'author', 'status', 'tag')
    search_fields = ('status', 'tag', 'author', 'date')
    list_filter = ('author', 'date', 'status', 'tag')


@admin.register(MobinetReport)
class MobinetReportAdmin(ReportAdmin):
    pass
