from rest_framework import serializers

from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super().__init__(many=many, *args, **kwargs)

    date = serializers.DateTimeField(format='%Y-%m-%d', required=False)

    class Meta:
        model = Report
        fields = ('text', 'author', 'author_name', 'date', 'status')
