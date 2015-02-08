from django.contrib import admin
from taggit.models import Tag
from forritun.models import ProgrammingLanguage, Resource, TagWithCategory, TaggedWithCategory


class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 3
    readonly_fields = ['date_created', 'date_modified', 'slug']


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    readonly_fields = ['date_created', 'date_modified', 'slug']
    inlines = [ResourceInline]
    list_filter = ['date_created']


class TaggedItemInline(admin.StackedInline):
    model = TaggedWithCategory


class TagAdmin(admin.ModelAdmin):
    inlines = [
        TaggedItemInline
    ]
    list_display = ["name", "slug", "category"]
    ordering = ["name", "slug", "category"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ["name"]}

admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)
admin.site.unregister(Tag)
admin.site.register(TagWithCategory, TagAdmin)