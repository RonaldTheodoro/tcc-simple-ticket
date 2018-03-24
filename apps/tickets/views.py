from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from . import forms, models


@method_decorator(login_required, name='dispatch')
class OpenTicketView(generic.FormView):
    form_class = forms.RegisterForm
    template_name = 'open_ticket.html'
    success_url = reverse_lazy('core:index')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            requester = self.get_user(request.user.get_username())
            executor = self.get_user(form.cleaned_data.get('executor'))
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            priority = form.cleaned_data.get('priority')
            files = request.FILES.getlist('files')

            ticket = self.save_ticket(title, requester)

            self.save_task(description, priority, ticket, requester, executor)

            if files:
                self.save_files(files, ticket)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_user(self, username):
        return models.User.objects.get(username=username)

    def save_ticket(self, description, requester):
        return models.Ticket.objects.create(
            description=description,
            requester=requester
        )

    def save_task(self, description, priority, ticket, requester, executor):
        return models.Task.objects.create(
            description=description,
            priority=priority,
            ticket=ticket,
            creator=requester,
            executor=executor
        )

    def save_files(self, files, ticket):
        for file in files:
            models.File.objects.create(file=file, ticket=ticket)


class TicketList(generic.ListView):
    model = models.Ticket
    template_name = 'list.html'


class TicketDetail(generic.DetailView):
    model = models.Ticket
    template_name = 'ticket_detail.html'


class TicketEdit(generic.UpdateView):
    model = models.Ticket
    template_name = 'ticket_edit.html'
    form_class = forms.TicketForm


def task_detail(request, ticket_pk, task_pk):
    ticket = get_object_or_404(models.Ticket, pk=ticket_pk,)
    task = get_object_or_404(ticket.task, pk=task_pk)
    return render(
        request,
        'task_detail.html',
        {'ticket': ticket, 'task': task}
    )
