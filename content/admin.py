from django.contrib import admin

from .models import Application, Project


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'creation')
    search_fields = ('name', 'creation', 'phone_number', 'email')
    list_filter = ('creation',)
    empty_value_display = '-пусто-'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description')
    search_fields = ('title', 'description')
    empty_value_display = '-пусто-'


admin.site.register(Project, ProjectAdmin)
admin.site.register(Application, ApplicationAdmin)
