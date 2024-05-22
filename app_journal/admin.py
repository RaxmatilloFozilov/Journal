from django.contrib import admin
from app_journal.models import Paper, Publication, JournalMain, PaperMain, Contacts


class PaperAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'author', 'year')
    search_fields = ('title', 'author', 'user', 'description', 'keywords', 'references')
    ordering = ('-year',)
    date_hierarchy = 'year'


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('journal_name_uz', 'journal_name_en', 'journal_description_uz', 'journal_description_en')
    search_fields = ('journal_name_uz', 'journal_name_en', 'journal_description_uz', 'journal_description_en')
    list_filter = ('journal_name_uz', 'journal_description_uz')


admin.site.register(Paper)
admin.site.register(Contacts)
admin.site.register(JournalMain)
admin.site.register(Publication)
admin.site.register(PaperMain)
# admin.site.register(Requirements)
# Register your models here.
