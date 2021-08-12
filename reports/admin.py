from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import MobinetReport, MoneyBack, Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('text', 'date', 'author', 'status', 'tag')
    search_fields = ('status', 'tag', 'author', 'date')
    list_filter = ('author', 'date', 'status', 'tag')
    actions = ['make_closed', 'make_delayed']

    @admin.action(description='Закрыть кейс')
    def make_closed(self, request, queryset):
        updated = queryset.update(status='Closed')
        self.message_user(request, ngettext(
            '%d кейс успешно закрыт.',
            '%d кейса успешно закрыто.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Отложить кейс')
    def make_delayed(self, request, queryset):
        updated = queryset.update(tag='Delayed')
        self.message_user(request, ngettext(
            '%d кейс успешно отложен.',
            '%d кейса успешно отложено.',
            updated,
        ) % updated, messages.SUCCESS)


@admin.register(MobinetReport)
class MobinetReportAdmin(ReportAdmin):
    pass


@admin.register(MoneyBack)
class MoneyBackAdmin(ReportAdmin):
    list_display = (
        'text', 'value', 'wallet', 'date', 'author', 'status', 'tag', 'link'
    )
    search_fields = ('status', 'tag', 'author', 'date', 'link')
    list_filter = ('author', 'date', 'status', 'tag', 'value')
