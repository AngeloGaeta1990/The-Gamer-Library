from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlatformList.as_view(), name='home'),
    path('add_game/', views.add_game, name='add_game'),
    path('add_platform/', views.add_platform, name='add_platform'),
    path('<int:user_id>/<slug:slug>/', views.platform_detail,
         name='platform_detail'),
    path('<int:user_id>/<slug:slug>/edit_platform/',
         views.edit_platform, name='edit_platform'),
    path('<int:user_id>/<slug:slug>/delete_platform/',
         views.delete_platform, name='delete_platform'),
    path('<int:user_id>/<slug:platform_slug>/<slug:game_slug>/',
         views.game_detail, name='game_detail'),
    path('<int:user_id>/<slug:platform_slug>/<slug:game_slug>/edit_game/',
         views.edit_game, name='edit_game'),
    path('<int:user_id>/<slug:platform_slug>/<slug:game_slug>/delete_game/',
         views.delete_game, name='delete_game'),
]
