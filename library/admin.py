from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Game, WishList, Platform


# Register your models here.
@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):
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
    list_display = ('name', 'slug', 'category', 'id', 'user')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['id', 'category', 'user',]


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'release_date', 'developer', 'get_platform',
                    'id')
    search_fields = ('game_name', 'developer', 'game_platform')

    def get_platform(self, obj):
        return obj.platform.platform_name if obj.platform else None

    get_platform.short_description = 'Platform'
