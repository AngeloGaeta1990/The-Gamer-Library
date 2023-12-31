from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Bio

# Register your models here.
@admin.register(Bio)
class BioAdmin(SummernoteModelAdmin):
    list_display = ('description', 'title')
    search_fields = ['title']
    summernote_fields = ('description',)
