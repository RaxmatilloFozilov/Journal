from django.contrib import admin
from app_journal.models import Paper, Publication, JournalMain, PaperMain, Contacts

admin.site.register(Paper)
admin.site.register(Contacts)
admin.site.register(JournalMain)
admin.site.register(Publication)
admin.site.register(PaperMain)
# Register your models here.
