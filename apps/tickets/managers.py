from django.db import models


class TicketManager(models.Manager):

    def create_ticket(self, description, requester):
        return self.create(description=description, requester=requester)

    def get_active_tickets(self):
        return self.filter(active=True)


class TaskManager(models.Manager):

    def create_task(self, description, priority, ticket, creator, executor):
        return self.create(
            description=description,
            priority=priority,
            ticket=ticket,
            creator=creator,
            executor=executor
        )


class FileManager(models.Manager):

    def create_file(self, file, ticket):
        return self.create(file=file, ticket=ticket)
