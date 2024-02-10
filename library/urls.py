from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlatformList.as_view(), name='home'),
    path('add_game/', views.add_game, name='add_game'),
    path('add_platform/', views.add_platform, name='add_platform'),
    path('add_wishlist/', views.add_wishlist, name='add_wishlist'),
    path('intro', views.intro, name='intro'),
    path('<int:user_id>/<slug:slug>/platform_detail', views.platform_detail,
         name='platform_detail'),
    path('<int:user_id>/<slug:platform_slug>/<slug:game_slug>/game_detail',
         views.game_detail, name='game_detail'),
    path('<int:user_id>/<slug:platform_slug>/<slug:wishlist_game_slug>/'
         'wishlist_game_detail', views.wishlist_game_detail,
         name='wishlist_game_detail'),
    path('<int:user_id>/<slug:slug>/edit_platform/',
         views.edit_platform, name='edit_platform'),
    path('<int:user_id>/<slug:platform_slug>/<slug:game_slug>/edit_game/',
         views.edit_game, name='edit_game'),
    path('<int:user_id>/<slug:platform_slug>/<slug:wishlist_game_slug>/'
         'edit_wishlist_game/', views.edit_wishlist_game,
         name='edit_wishlist_game'),
    path('<int:user_id>/<slug:platform_slug>/<slug:game_slug>/delete_game/',
         views.delete_game, name='delete_game'),
    path('<int:user_id>/<slug:slug>/delete_platform/',
         views.delete_platform, name='delete_platform'),
    path('<int:user_id>/<slug:platform_slug>/<slug:wishlist_game_slug>/'
         'delete_wishlist_game/', views.delete_wishlist_game,
         name='delete_wishlist_game'),
]
