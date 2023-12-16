from django.contrib import admin
from .models import UserProfile, Game, WishList, FriendList

# Register your models here.

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_friends', 'get_games', 'get_wishlist')

    def get_friends(self, obj):
        return ', '.join([friend.username for friend in obj.friends.all()])
    get_friends.short_description = 'Friends'

    def get_games(self, obj):
        return ', '.join([game.game_name for game in obj.games.all()])
    get_games.short_description = 'Played Games'

    def get_wishlist(self, obj):
        return ', '.join([wishlist.game_name for wishlist in obj.wishlist.all()])
    get_wishlist.short_description = 'Wishlist'

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'user_score', 'metacritic_score', 'release_date','completion_date', 'developer', 'platform',)
    filter_horizontal = ('players',)

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'release_date', 'developer', 'platform')
    filter_horizontal = ('players',)

@admin.register(FriendList)
class FriendListAdmin(admin.ModelAdmin):
    list_display = ('user', 'friend')

