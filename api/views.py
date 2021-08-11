import django_filters.rest_framework
from rest_framework import generics, status
from rest_framework.response import Response

from reports.models import Report, MobinetReport, MoneyBack
from .serializers import (ReportSerializer,
                          MobinetReportSerializer,
                          MoneybackSerializer)


class ReportList(generics.ListCreateAPIView, generics.UpdateAPIView):
    queryset = Report.objects.all().exclude(status='Closed')
    serializer_class = ReportSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['status', 'tag', ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class MobinetReportList(ReportList):
    queryset = MobinetReport.objects.all().exclude(status='Closed')
    serializer_class = MobinetReportSerializer


class MoneybackAPIView(ReportList):
    queryset = MoneyBack.objects.all().exclude(status='Closed')
    serializer_class = MoneybackSerializer
