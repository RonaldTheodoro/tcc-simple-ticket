from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from .forms import ReportForm
from .models import Report


@method_decorator(login_required, name='dispatch')
class ReportList(generic.ListView):
    model = Report
    template_name = 'reports/list.html'
    context_object_name = 'reports'


@method_decorator(login_required, name='dispatch')
class ReportDetail(generic.DetailView):
    model = Report
    template_name = 'reports/detail.html'


@method_decorator(login_required, name='dispatch')
class ReportNew(generic.FormView):
    form_class =  ReportForm
    template_name = 'reports/new.html'
    success_url = reverse_lazy('reports:list')
