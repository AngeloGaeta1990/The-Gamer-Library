from django.contrib import admin
from .models import UserProfile, Game, WishList, Platform, FriendList

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'user_score', 'metacritic_score', 'release_date', 'completion_date', 'developer', 'get_platform')
    search_fields = ('game_name', 'developer', 'platform')
    list_filter = ('platform',)

    def get_platform(self, obj):
        return obj.platform.platform_name if obj.platform else None

    get_platform.short_description = 'Platform'

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('platform_name',)
    search_fields = ('platform_name',)

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'release_date', 'developer', 'get_platform')
    search_fields = ('game_name', 'developer', 'platform')

    def get_platform(self, obj):
        return obj.platform.platform_name if obj.platform else None

    get_platform.short_description = 'Platform'

@admin.register(FriendList)
class FriendListAdmin(admin.ModelAdmin):
    list_display = ('user', 'friend')
    search_fields = ('user__username', 'friend__username')
