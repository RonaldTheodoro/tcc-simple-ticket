from django.urls import reverse_lazy
from django.views import generic

from .forms import ReportForm
from .models import Report


class ReportList(generic.ListView):
    model = Report
    template_name = 'reports/list.html'
    context_object_name = 'reports'


class ReportDetail(generic.DetailView):
    model = Report
    template_name = 'reports/detail.html'


class ReportNew(generic.FormView):
    form_class =  ReportForm
    template_name = 'reports/new.html'
    success_url = reverse_lazy('reports:list')

