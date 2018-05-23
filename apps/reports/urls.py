from django.urls import path

from . import views


app_name = 'reports'

urlpatterns = [
    path('', views.ReportList.as_view(), name='report_list'),
    path('<int:pk>/', views.ReportDetail.as_view(), name='report_detail'),
]
