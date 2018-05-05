from django.contrib import admin

from .models import Ticket, Task, Log, File


admin.site.register(Ticket)
admin.site.register(Task)
admin.site.register(Log)
admin.site.register(File)
