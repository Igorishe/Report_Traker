import datetime

from django.contrib import admin, messages
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext

from .models import MobinetReport, MoneyBack, Report


class IsClosedListFilter(admin.SimpleListFilter):
    title = _('Дополнительные фильтры')
    parameter_name = 'is-status-closed'

    def lookups(self, request, model_admin):
        return (
            ('opened', _('Открытые')),
            ('just-closed', _('Недавно закрытые')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'opened':
            return queryset.exclude(status='Closed')
        if self.value() == 'just-closed':
            lookup_date = timezone.now() - datetime.timedelta(days=2)
            return queryset.filter(last_edit__gt=lookup_date).filter(
                status='Closed'
            )


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('text', 'date', 'last_edit', 'author', 'status', 'tag')
    search_fields = ('status', 'tag', 'author', 'date')
    list_filter = (
        IsClosedListFilter, 'status', 'tag', 'last_edit', 'date', 'author'
    )
    actions = ['make_closed', 'make_delayed']

    @admin.action(description='Закрыть кейс')
    def make_closed(self, request, queryset):
        updated = queryset.update(
            status='Closed',
            last_edit=datetime.datetime.now()
        )
        self.message_user(request, ngettext(
            '%d кейс успешно закрыт.',
            '%d кейса успешно закрыто.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Отложить кейс')
    def make_delayed(self, request, queryset):
        updated = queryset.update(
            tag='Delayed',
            last_edit=datetime.datetime.now()
        )
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
    list_filter = (
        'author', 'date', 'status', 'tag', 'value', IsClosedListFilter
    )
