from django.views import generic

from apps.tickets.models import Report


class ReportList(generic.ListView):
    model = Report
    template_name = 'reports/list.html'
    context_object_name = 'reports'


class ReportDetail(generic.DetailView):
    model = Report
    template_name = 'reports/detail.html'
