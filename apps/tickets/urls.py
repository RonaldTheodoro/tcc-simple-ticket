from django.urls import path

from . import views


app_name = 'tickets'

urlpatterns = [
    path('', views.TicketList.as_view(), name='list'),
    path('<int:pk>/', views.TicketDetail.as_view(), name='detail'),
    path('<int:pk>/edit/', views.TicketEdit.as_view(), name='ticket_edit'),
    path(
        '<int:ticket_pk>/task/<int:task_pk>/',
        views.task_detail,
        name='task_detail'
    ),
    path('new_ticket/', views.OpenTicketView.as_view(), name='new_ticket'),
]
