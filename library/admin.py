from django.contrib import admin
from .models import Game, WishList, Platform, PCPlatform, ConsolePlatform, ServicePlatform, MobilePlatform
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):
    list_display = ('name', 'user_score', 'metacritic_score', 'release_date', 'completion_date', 'developer', 'get_platform')
    search_fields = ['name']
    list_filter = ('platform',)
    summernote_fields = ('user_review',)

    def get_platform(self, obj):
        return obj.platform.platform_name if obj.platform else None

    get_platform.short_description = 'Platform'



# @admin.register(CustomUser)
# class CustomUserAdmin(BaseUserAdmin):
#     list_display = ('username', 'email')
#     search_fields = ('username', 'email')


# @admin.register(Game)
# class GameAdmin(admin.ModelAdmin):
#     list_display = ('game_name', 'user_score', 'metacritic_score', 'release_date', 'completion_date', 'developer', 'get_platform')
#     search_fields = ('game_name', 'developer', 'platform')
#     list_filter = ('platform',)

#     def get_platform(self, obj):
#         return obj.platform.platform_name if obj.platform else None

#     get_platform.short_description = 'Platform'

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'games')
    search_fields = ['name']
    list_filter = ['category']



@admin.register(PCPlatform)
class PCPlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'operative_systems', 'gpu', 'cpu', 'ram')
    search_fields = ['name']

@admin.register(ConsolePlatform)
class ConsolePlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'model')
    search_fields = ['name']
    # Add other configurations as needed

@admin.register(ServicePlatform)
class ServicePlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subscription_fee', 'plan')
    search_fields = ['name']
    # Add other configurations as needed

@admin.register(MobilePlatform)
class MobilePlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'operative_systems')
    search_fields = ['name']

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'release_date', 'developer', 'get_platform')
    search_fields = ('game_name', 'developer', 'game_platform')

    def get_platform(self, obj):
        return obj.platform.platform_name if obj.platform else None

    get_platform.short_description = 'Platform'

# @admin.register(FriendList)
# class FriendListAdmin(admin.ModelAdmin):
#     list_display = ('user', 'friend')
#     search_fields = ('user__username', 'friend__username')

#     def user(self, obj):
#         return obj.user.username

#     def friend(self, obj):
#         return obj.friend.username
