import os

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from model_utils import Choices, fields
from model_utils.models import TimeStampedModel


def get_filename_ext(filepath):
    """Return a basename from a filepath"""
    basename = os.path.basename(filepath)
    return os.path.splitext(basename)


def upload_file_path(instance, filename):
    """Return upload path"""
    name, ext = get_filename_ext(filename)
    new_filename = hash(name)
    ticket_pk = instance.ticket.pk
    return f'files/{ticket_pk}/{ticket_pk}-{new_filename}{ext}'


User = get_user_model()


class Ticket(TimeStampedModel):
    """Stores a single ticket, related to :model:`auth.User`"""
    description = models.CharField('description', max_length=255)
    active = models.BooleanField('active', default=True)
    finished_at = fields.MonitorField(
        'finished at',
        default=None,
        blank=True,
        null=True,
        monitor='active',
        when=[False]
    )
    requester = models.ForeignKey(
        User,
        verbose_name='requester',
        related_name='ticket',
        on_delete=models.PROTECT
    )

    class Meta:
        ordering = ['-created', 'active']

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        """Return the ticket absolute url"""
        return reverse('tickets:ticket_detail', kwargs={'pk': self.pk})


class Task(TimeStampedModel):
    """Stores a single task, related to :model:`tickets.Ticket` :model:`auth.User`"""
    STATUS = Choices('low', 'medium', 'high')

    description = models.CharField('description', max_length=5000)
    priority = fields.StatusField('priority')
    active = models.BooleanField('active', default=True)
    finished_at = fields.MonitorField(
        'finished at',
        default=None,
        blank=True,
        null=True,
        monitor='active',
        when=[False]
    )
    ticket = models.ForeignKey(
        'Ticket',
        verbose_name='task',
        related_name='task',
        on_delete=models.PROTECT
    )
    creator = models.ForeignKey(
        User,
        verbose_name='creator',
        related_name='creator',
        on_delete=models.PROTECT
    )
    executor = models.ForeignKey(
        User,
        verbose_name='executor',
        related_name='executor',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        """Return the task absolute url"""
        return reverse(
            'tickets:task_detail',
            kwargs={'ticket_pk': self.ticket.pk, 'task_pk': self.pk}
        )


class Log(TimeStampedModel):
    """Stores a single log, related to :model:`tickets.Task`"""
    description = models.CharField('description', max_length=5000)
    task = models.ForeignKey(
        'Task',
        verbose_name='task',
        related_name='logs',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.description


class File(models.Model):
    """Stores a single file, related to :model:`tickets.Ticket`"""
    file = models.FileField('file', upload_to=upload_file_path)
    ticket = models.ForeignKey(
        'Ticket',
        verbose_name='ticket',
        related_name='files',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.ticket.description
