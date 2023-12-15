from django.contrib import admin
from .models import User, Game, WishList, UserGame, UserWishList, FriendList

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password']

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'game_name', 'user_score', 'metacritic_score', 'genres', 'release_date', 'developer', 'platform']

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ['id', 'game_name', 'genres', 'stores', 'release_date', 'platform', 'developer']

@admin.register(UserGame)
class UserGameAdmin(admin.ModelAdmin):
    list_display = ['user', 'game']

@admin.register(UserWishList)
class UserWishListAdmin(admin.ModelAdmin):
    list_display = ['user', 'game']

@admin.register(FriendList)
class FriendListAdmin(admin.ModelAdmin):
    list_display = ['user', 'friend']