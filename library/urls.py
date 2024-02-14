from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlatformList.as_view(), name='home'),
    path('add_game/', views.add_game, name='add_game'),
    path('add_platform/', views.add_platform, name='add_platform'),
    path('add_wishlist/', views.add_wishlist, name='add_wishlist'),
    path('info', views.info, name='info'),
    path('intro', views.intro, name='intro'),
    path('user_<int:user_id>/platform_<uuid:platform_id>/game_<uuid:game_id>/'
         'delete_game/', views.delete_game, name='delete_game'),
    path('user_<int:user_id>/platform_<uuid:platform_id>/delete_platform/',
         views.delete_platform, name='delete_platform'),
    path('user_<int:user_id>/platform_<uuid:platform_id>/'
         'wishlist_<uuid:wishlist_game_id>/delete_wishlist_game/',
         views.delete_wishlist_game, name='delete_wishlist_game'),
    path('user_<int:user_id>/platform_<uuid:platform_id>/edit_platform/',
         views.edit_platform, name='edit_platform'),
    path('user_<int:user_id>/platform<uuid:platform_id>/'
         'game_<uuid:game_id>/edit_game/',
         views.edit_game, name='edit_game'),
    path('user_<int:user_id>/platform_<uuid:platform_id>/'
         'wishlist_<uuid:wishlist_game_id>/'
         'edit_wishlist_game/', views.edit_wishlist_game,
         name='edit_wishlist_game'),
    path('user_<int:user_id>/platform_<uuid:platform_id>/game_<uuid:game_id>/'
         'game_detail', views.game_detail, name='game_detail'),
    path('user_<int:user_id>/platform_<uuid:platform_id>/platform_detail',
         views.platform_detail, name='platform_detail'),
    path('user_<int:user_id>/platform_<uuid:platform_id>/'
         'wishlist_<uuid:wishlist_game_id>/wishlist_game_detail',
         views.wishlist_game_detail, name='wishlist_game_detail'),
]
