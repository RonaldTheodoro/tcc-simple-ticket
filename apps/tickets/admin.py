from django.contrib import admin

from .models import Ticket, Task, Log, File, Report


admin.site.register(Ticket)
admin.site.register(Task)
admin.site.register(Log)
admin.site.register(File)
admin.site.register(Report)
