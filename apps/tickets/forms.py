from django import forms

from .models import User, Ticket, Task, Log


class RegisterForm(forms.Form):
    PRIORITIES = (
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
    )
    title = forms.CharField(max_length=255)
    description = forms.CharField(
        max_length=5000,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    priority = forms.ChoiceField(choices=PRIORITIES)
    executor = forms.ModelChoiceField(queryset=User.objects.all())
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False
    )


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('description', 'active', )


class TicketCloseForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('close_reason', )


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('description', 'priority', 'executor', )


class TaskLogForm(forms.ModelForm):

    class Meta:
        model = Log
        fields = ('description', )
