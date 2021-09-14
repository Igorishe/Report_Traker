from rest_framework import serializers

from reports.models import MobinetReport, MoneyBack, Report


class ReportSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d', required=False)
    last_edit = serializers.DateTimeField(format='%Y-%m-%d', required=False)
    id = serializers.IntegerField(source='pk', required=False)

    class Meta:
        model = Report
        fields = ('id', 'text', 'author', 'author_name', 'date', 'status',
                  'tag', 'last_edit')


class MobinetReportSerializer(ReportSerializer):
    class Meta:
        model = MobinetReport
        fields = ('id', 'text', 'author', 'author_name', 'date', 'status',
                  'tag', 'last_edit')


class MoneybackSerializer(ReportSerializer):
    class Meta:
        model = MoneyBack
        fields = ('id', 'text', 'author', 'author_name', 'date', 'last_edit',
                  'status', 'tag', 'value', 'wallet', 'link', 'payment_system')
