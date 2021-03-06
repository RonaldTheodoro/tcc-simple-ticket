from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from .forms import RegisterForm, TaskForm, TaskLogForm, TicketForm, TicketCloseForm
from .models import File, Log, Task, Ticket, User


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


@method_decorator(login_required, name='dispatch')
class TicketList(generic.ListView):
    model = Ticket
    template_name = 'tickets/list.html'
    context_object_name = 'tickets'


@method_decorator(login_required, name='dispatch')
class TicketDetail(generic.DetailView):
    model = Ticket
    template_name = 'tickets/detail.html'


@method_decorator(login_required, name='dispatch')
class TicketEdit(generic.UpdateView):
    model = Ticket
    template_name = 'tickets/edit.html'
    form_class = TicketForm

    def get_object(self, queryset=None):
        obj = super(TicketEdit, self).get_object(queryset)

        if not obj.active:
            raise Http404

        return obj


@login_required
def ticket_close(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    if not ticket.active:
        raise Http404

    open_tasks = []
    for task in ticket.tasks.all():
        if task.active:
            open_tasks.append(task)

    if len(open_tasks) > 0:
        context = {'ticket_pk': pk, 'tasks': open_tasks}
        return render(request, 'tickets/close.html', context)

    if request.method == 'POST':
        form = TicketCloseForm(request.POST)
        if form.is_valid():
            ticket.close_reason = form.cleaned_data.get('close_reason')
            ticket.active = False
            ticket.save()
            return HttpResponseRedirect(
                reverse('tickets:detail', kwargs={'pk': ticket.pk})
            )
    else:
        form = TicketCloseForm()
    return render(request, 'tickets/close.html', {'form': form})


@login_required
def task_detail(request, ticket_pk, task_pk):
    ticket = Ticket.objects.get_ticket(ticket_pk)
    task = Task.objects.get_task(ticket_pk, task_pk)
    context = {'ticket': ticket, 'task': task}
    return render(request, 'tasks/detail.html', context)


@login_required
def task_new(request, ticket_pk):
    ticket = Ticket.objects.get_ticket(ticket_pk)

    if not ticket.active:
        raise Http404

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            creator = User.objects.get(username=request.user.get_username())
            Task.objects.create_task(
                description=form.cleaned_data.get('description'),
                priority=form.cleaned_data.get('priority'),
                ticket=ticket,
                creator=creator,
                executor=form.cleaned_data.get('executor')
            )
            return HttpResponseRedirect(
                reverse('tickets:detail', kwargs={'pk': ticket_pk})
            )
    else:
        form = TaskForm()
    context = {'form': form, 'ticket_pk': ticket_pk}
    return render(request, 'tasks/new.html', context)


@login_required
def task_log(request, ticket_pk, task_pk):
    task = Task.objects.get_task(ticket_pk, task_pk)

    if not task.active:
        raise Http404

    if request.method == 'POST':
        form = TaskLogForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data.get('description')
            Log.objects.create(description=description, task=task)
            url = reverse(
                'tickets:task_detail',
                kwargs={'ticket_pk': ticket_pk, 'task_pk': task_pk}
            )
            return HttpResponseRedirect(url)
    else:
        form = TaskLogForm()
    context = {'form': form, 'ticket_pk': ticket_pk, 'task_pk': task_pk}
    return render(request, 'tasks/new_log.html', context)


@login_required
def task_close(request, ticket_pk, task_pk):
    task = Task.objects.get_task(ticket_pk, task_pk)

    if not task.active:
        raise Http404

    if request.method == 'POST':
        form = TaskLogForm(request.POST)
        if form.is_valid():
            Log.objects.create(
                description=form.cleaned_data.get('description'),
                task=task
            )
            task.active = False
            task.save()
            return HttpResponseRedirect(
                reverse(
                    'tickets:task_detail',
                    kwargs={'ticket_pk': ticket_pk, 'task_pk': task_pk}
                )
            )
    else:
        form = TaskLogForm()
    context = {'form': form, 'ticket_pk': ticket_pk, 'task_pk': task_pk}
    return render(request, 'tasks/close.html', context)
