from . import views
from django.urls import path

urlpatterns = [
    path('', views.PlatformList.as_view(), name='home'),
    path('add_game/', views.add_game, name='add_game'),
    path('add_platform/', views.add_platform, name='add_platform'),
    path('<slug:slug>/', views.platform_detail, name='platform_detail'),
    path('<slug:slug>/edit_platform/<uuid:platform_id>/',
         views.edit_platform, name='edit_platform'),
    path('<slug:slug>/delete_platform/<uuid:platform_id>/',
         views.delete_platform, name='delete_platform'),
]
