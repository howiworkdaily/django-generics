from django.contrib import admin
from models import Entry, ContentItemBase


class EntryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','content_type', 'object_id', 'publish_on', 'tags')
    search_fields = ('title', 'description', 'tags')

admin.site.register(Entry, EntryAdmin)
