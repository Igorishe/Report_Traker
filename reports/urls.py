from django.urls import path

from . import views

urlpatterns = [
    path('celery-check/', views.check, name='celery-check'),
    path('', views.index, name='index'),
]
