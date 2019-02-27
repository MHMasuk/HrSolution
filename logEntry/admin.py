from django.contrib import admin
from .models import Project, Entry

# Register your models here.


class EntryModelAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'task_date', 'working_hour',)
    search_fields = ('user__username', 'project__project_name', 'task_date', 'working_hour')


admin.site.register(Project)
admin.site.register(Entry, EntryModelAdmin)

