from django.db import models
from django.shortcuts import get_object_or_404


class TicketManager(models.Manager):

    def create_ticket(self, description, requester):
        return self.create(description=description, requester=requester)

    def get_active_tickets(self):
        return self.filter(active=True)

    def get_ticket(self, pk):
        return get_object_or_404(self, pk=pk)

class TaskManager(models.Manager):

    def create_task(self, description, priority, ticket, creator, executor):
        return self.create(
            description=description,
            priority=priority,
            ticket=ticket,
            creator=creator,
            executor=executor
        )

    def get_task(self, ticket_pk, task_pk):
        return get_object_or_404(self, ticket=ticket_pk, pk=task_pk)


class FileManager(models.Manager):

    def create_file(self, file, ticket):
        return self.create(file=file, ticket=ticket)
