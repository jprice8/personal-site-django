from django.contrib import admin
from django.db import models
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'short_description']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Project, ProjectAdmin)
