from django.contrib import admin
from class_schedule_app.models import SessionDate, Location, Session

# Register your models here.
admin.site.register(SessionDate)
admin.site.register(Location)
admin.site.register(Session)
