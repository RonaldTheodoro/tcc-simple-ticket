from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel

from apps.tickets.models import Ticket


class Report(TimeStampedModel):
    title = models.CharField('title', max_length=200)
    description = models.TextField('description')
    tickets = models.ManyToManyField(
        Ticket,
        verbose_name='tickets',
        related_name='reports'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return the task absolute url"""
        return reverse('reports:report_detail', kwargs={'pk': self.pk})
