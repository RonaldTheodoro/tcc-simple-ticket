from django.urls import path

from . import views


app_name = 'reports'

urlpatterns = [
    path('', views.ReportList.as_view(), name='list'),
    path('<int:pk>/', views.ReportDetail.as_view(), name='detail'),
    path('<int:pk>/edit', views.ReportEdit.as_view(), name='edit'),
    path('new/', views.ReportNew.as_view(), name='new'),
]
