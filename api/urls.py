from django.urls import path
from rest_framework.authtoken import views

from .views import MobinetReportList, MoneybackAPIView, ReportList

urlpatterns = [
    path('auth/', views.obtain_auth_token, name='authorization'),
    path('v1/reports/', ReportList.as_view(), name='reports'),
    path('v1/mn-reports/', MobinetReportList.as_view(), name='mn-reports'),
    path('v1/moneybacks/', MoneybackAPIView.as_view(), name='moneybacks'),
    path(
        'v1/moneybacks/<int:pk>/',
        MoneybackAPIView.as_view(),
        name='moneyback-update'
    ),
]
