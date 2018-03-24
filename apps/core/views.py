from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from apps.tickets import models

from . import forms


@login_required
def index(request):
    tickets = get_list_or_404(models.Ticket, active=True)
    return render(request, 'index.html', {'object_list': tickets})


def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:index')

    else:
        form = forms.SignUpForm()
    return render(request, 'signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = models.User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user
