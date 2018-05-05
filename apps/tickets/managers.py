from django.db import models


class TicketManager(models.Manager):

    def get_active_tickets(self):
        return self.filter(active=True)
