from django.contrib import admin

from .models import Application, Project, Tag, Questions, CompanyData


class CompanyDataAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'creation')
    search_fields = ('name', 'creation', 'phone_number', 'email')
    list_filter = ('creation',)
    empty_value_display = '-пусто-'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('num', 'title', 'description')
    search_fields = ('title', 'description')
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    empty_value_display = '-пусто-'


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('num', 'question')
    search_fields = ('num', 'question')


admin.site.register(CompanyData, CompanyDataAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Questions, QuestionsAdmin)
