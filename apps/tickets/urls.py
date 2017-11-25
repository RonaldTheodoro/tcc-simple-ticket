from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.TicketDetail.as_view(), name='detail'),
    url(r'^new_ticket/$', views.OpenTicketView.as_view(), name='new_ticket'),
]
