from django.db import models
from django.shortcuts import get_object_or_404


class TicketManager(models.Manager):
    """Ticket Manager"""

    def create_ticket(self, description, requester):
        """Create a ticket register"""
        return self.create(description=description, requester=requester)

    def get_active_tickets(self):
        """Get all open tickets"""
        return self.filter(active=True)

    def get_ticket(self, pk):
        """Get a ticket register"""
        return get_object_or_404(self, pk=pk)

class TaskManager(models.Manager):
    """Task Manager"""

    def create_task(self, description, priority, ticket, creator, executor):
        """Create a task register"""
        return self.create(
            description=description,
            priority=priority,
            ticket=ticket,
            creator=creator,
            executor=executor
        )

    def get_task(self, ticket_pk, task_pk):
        """Get a task register"""
        return get_object_or_404(self, ticket=ticket_pk, pk=task_pk)


class FileManager(models.Manager):
    """File Manager"""

    def create_file(self, file, ticket):
        """Create a file register"""
        return self.create(file=file, ticket=ticket)
