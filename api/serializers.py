from rest_framework import serializers

from reports.models import Report, MobinetReport


class ReportSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d', required=False)

    class Meta:
        model = Report
        fields = ('text', 'author', 'author_name', 'date', 'status', 'tag')


class MobinetReportSerializer(ReportSerializer):
    class Meta:
        model = MobinetReport
        fields = ('text', 'author', 'author_name', 'date', 'status', 'tag')
