from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, render

from apps.tickets import models


@login_required
def index(request):
    tickets = get_list_or_404(models.Ticket, active=True)
    return render(request, 'core/index.html', {'object_list': tickets})
