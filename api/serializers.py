from rest_framework import serializers

from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d', required=False)

    class Meta:
        model = Report
        fields = ('text', 'author', 'author_name', 'date', 'status')
