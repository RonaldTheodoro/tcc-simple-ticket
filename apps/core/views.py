from django.shortcuts import render, get_list_or_404
from apps.tickets import models


def index(request):
    tickets = get_list_or_404(models.Ticket)  # , active=True)
    return render(request, 'core/index.html', {'tickets': tickets})
