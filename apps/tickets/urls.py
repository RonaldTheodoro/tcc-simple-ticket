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
    path('<int:ticket_pk>/task/new', views.task_new, name='task_new'),
    path(
        '<int:ticket_pk>/task/<int:task_pk>/new_log',
        views.task_log,
        name='task_log'
    ),
    path('new/', views.OpenTicketView.as_view(), name='new'),
]
