from django.urls import path

from . import views


app_name = 'tickets'

urlpatterns = [
    path('', views.TicketList.as_view(), name='list'),
    path('<int:pk>/', views.TicketDetail.as_view(), name='detail'),
    path('<int:pk>/edit/', views.TicketEdit.as_view(), name='edit'),
    path(
        '<int:ticket_pk>/task/<int:task_pk>/',
        views.task_detail,
        name='task_detail'
    ),
    path('new/', views.OpenTicketView.as_view(), name='new'),
    path('reports/', views.ReportList.as_view(), name='report_list'),
    path(
        'reports/<int:pk>/',
        views.ReportDetail.as_view(),
        name='report_detail'
    ),
]
