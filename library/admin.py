from django.contrib import admin
from .models import (Game, WishList, Platform, PCPlatform,
                     ConsolePlatform, ServicePlatform, MobilePlatform)
from django_summernote.admin import SummernoteModelAdmin


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
    list_display = ('name', 'slug', 'category', "id")
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['id', 'category']


@admin.register(PCPlatform)
class PCPlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'operative_systems', 'gpu',
                    'cpu', 'ram', 'id')
    search_fields = ['name']


@admin.register(ConsolePlatform)
class ConsolePlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'model', 'id')
    search_fields = ['name']


@admin.register(ServicePlatform)
class ServicePlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'subscription_fee', 'plan',
                    'id')
    search_fields = ['name']


@admin.register(MobilePlatform)
class MobilePlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'brand', 'operative_systems',
                    'id')
    search_fields = ['name']


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'release_date', 'developer', 'get_platform',
                    'id')
    search_fields = ('game_name', 'developer', 'game_platform')

    def get_platform(self, obj):
        return obj.platform.platform_name if obj.platform else None

    get_platform.short_description = 'Platform'
