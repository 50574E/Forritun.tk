from django.contrib import admin
from forritun.models import ProgrammingLanguage, Resource


class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 3
    readonly_fields = ['date_created', 'date_modified', 'slug']


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    readonly_fields = ['date_created', 'date_modified', 'slug']
    inlines = [ResourceInline]
    list_filter = ['date_created']


admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)
