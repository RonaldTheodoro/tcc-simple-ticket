import os

from django.contrib.auth import get_user_model
from django.db import models
from model_utils import Choices, fields
from model_utils.models import TimeStampedModel


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    return os.path.splitext(basename)


def upload_file_path(instance, filename):
    name, ext = get_filename_ext(filename)
    new_filename = hash(name)
    pk = instance.ticket.pk
    return f'files/{pk}/{pk}-{new_filename}{ext}'


User = get_user_model()


class Ticket(TimeStampedModel):
    description = models.CharField('description', max_length=255)
    active = models.BooleanField('active', default=True)
    requester = models.ForeignKey(
        User,
        verbose_name='requester',
        related_name='ticket'
    )

    def __str__(self):
        return self.description


class Task(TimeStampedModel):
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
        verbose_name='ticket',
        related_name='ticket'
    )
    creator = models.ForeignKey(
        User,
        verbose_name='creator',
        related_name='creator'
    )
    executor = models.ForeignKey(
        User,
        verbose_name='executor',
        related_name='executor'
    )

    def __str__(self):
        return self.description


class Log(TimeStampedModel):
    description = models.CharField('description', max_length=5000)
    task = models.ForeignKey(
        'Task',
        verbose_name='task',
        related_name='logs'
    )

    def __str__(self):
        return self.description


class File(models.Model):
    file = models.FileField('file', upload_to=upload_file_path)
    ticket = models.ForeignKey(
        'Ticket',
        verbose_name='ticket',
        related_name='files'
    )

    def __str__(self):
        return self.ticket.description
