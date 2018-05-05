from django.db import models


class TicketManager(models.Manager):

    def create_ticket(self, description, requester):
        return self.create(description=description, requester=requester)

    def get_active_tickets(self):
        return self.filter(active=True)
