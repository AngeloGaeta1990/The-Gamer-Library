from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Game, WishListGame, Platform


# Register your models here.
@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):
    """
    Admin class for Game model.
    """
    list_display = ('name', 'user_score', 'metacritic_score', "id",
                    'release_date', 'completion_date', 'developer',
                    'get_platform')
    search_fields = ['name']
    list_filter = ['id', 'platform', 'platform__id']
    summernote_fields = ('user_review')

    def get_platform(self, obj):
        return obj.platform.name if obj.platform else None

    get_platform.short_description = 'Platform'


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    """
    Admin class for Platform model.
    """
    list_display = ('name', 'slug', 'category', 'id', 'user')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['id', 'category', 'user',]


@admin.register(WishListGame)
class WishListAdmin(admin.ModelAdmin):
    """
    Admin class for WishListGame model.
    """
    list_display = ('name', 'release_date', 'developer', 'get_platform',
                    'id')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'developer', 'platform')

    def get_platform(self, obj):
        return obj.platform.name if obj.platform else None

    get_platform.short_description = 'Platform'
