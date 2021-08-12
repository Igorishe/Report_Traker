from rest_framework import serializers

from reports.models import MobinetReport, MoneyBack, Report


class ReportSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d', required=False)
    id = serializers.IntegerField(source='pk', required=False)

    class Meta:
        model = Report
        fields = ('id', 'text', 'author', 'author_name', 'date', 'status',
                  'tag')


class MobinetReportSerializer(ReportSerializer):
    class Meta:
        model = MobinetReport
        fields = ('id', 'text', 'author', 'author_name', 'date', 'status',
                  'tag')


class MoneybackSerializer(ReportSerializer):
    wallet = serializers.CharField(required=False)

    class Meta:
        model = MoneyBack
        fields = ('id', 'text', 'author', 'author_name', 'date', 'status',
                  'tag', 'value', 'wallet', 'link')
