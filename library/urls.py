from . import views
from django.urls import path

urlpatterns = [
    path('add_game/', views.add_game, name='add_game'),
    path('add_platform/', views.add_platform, name='add_platform'),
    path('<slug:slug>/', views.platform_detail, name = 'platform_detail'),
    path('', views.PlatformList.as_view(), name='home')
]