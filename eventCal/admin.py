from django.contrib import admin
from eventCal.models.Events import SubjectEvent,PersonalEvent
from eventCal.models.Semester import Semester




admin.site.register(SubjectEvent)
admin.site.register(PersonalEvent)

class SemesterAdmin(admin.ModelAdmin):
    list_display = ('start_date','end_date','is_even')

admin.site.register(Semester,SemesterAdmin)


