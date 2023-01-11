from django.contrib import admin

from GenratedTimeTable.models import TimeTable, TimeTable_Slot

# Register your models here.
admin.site.register(TimeTable_Slot)
admin.site.register(TimeTable)
