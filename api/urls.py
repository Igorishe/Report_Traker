from django.urls import path
from rest_framework.authtoken import views


from .views import ReportList


urlpatterns = [
    path('auth/', views.obtain_auth_token),
    path('v1/report/', ReportList.as_view()),
]
