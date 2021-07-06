from rest_framework import generics
import django_filters.rest_framework

from reports.models import Report
from .serializers import ReportSerializer


class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['status', ]
