from django.urls import path, include

from .views import ReportList


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('v1/report/', ReportList.as_view()),
]
