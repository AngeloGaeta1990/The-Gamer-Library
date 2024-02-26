from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Bio, CollaborateRequest


# Register your models here.
@admin.register(Bio)
class BioAdmin(SummernoteModelAdmin):
    """
    Admin class for Bio model.
    """

    list_display = ('description', 'title')
    search_fields = ['title']
    summernote_fields = ('description',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin class for CollaborateRequest model.
    """

    list_display = ('message', 'read',)
