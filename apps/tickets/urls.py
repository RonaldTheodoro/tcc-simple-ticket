from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TicketList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.TicketDetail.as_view(), name='detail'),
    url(
        r'^(?P<pk>\d+)/edit/$',
        views.TicketEdit.as_view(),
        name='ticket_edit'
    ),
    url(
        r'^(?P<ticket_pk>\d+)/task/(?P<task_pk>\d+)/$',
        views.task_detail,
        name='task_detail'
    ),
    url(r'^new_ticket/$', views.OpenTicketView.as_view(), name='new_ticket'),
]
