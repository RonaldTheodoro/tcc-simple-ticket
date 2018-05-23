from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from .models import User, Ticket, Task, File
from .forms import RegisterForm, TicketForm


@method_decorator(login_required, name='dispatch')
class OpenTicketView(generic.FormView):
    form_class = RegisterForm
    template_name = 'tickets/new.html'
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
        return User.objects.get(username=username)

    def save_ticket(self, description, requester):
        return Ticket.objects.create_ticket(description, requester)

    def save_task(self, description, priority, ticket, requester, executor):
        return Task.objects.create_task(
            description,
            priority,
            ticket,
            requester,
            executor
        )

    def save_files(self, files, ticket):
        for file in files:
            File.objects.create_file(file, ticket)


class TicketList(generic.ListView):
    model = Ticket
    template_name = 'tickets/list.html'
    context_object_name = 'tickets'


class TicketDetail(generic.DetailView):
    model = Ticket
    template_name = 'tickets/detail.html'


class TicketEdit(generic.UpdateView):
    model = Ticket
    template_name = 'tickets/edit.html'
    form_class = TicketForm


def task_detail(request, ticket_pk, task_pk):
    ticket = Ticket.objects.get_ticket(ticket_pk)
    task = Task.objects.get_task(ticket_pk, task_pk)
    return render(
        request,
        'tasks/detail.html',
        {'ticket': ticket, 'task': task}
    )
