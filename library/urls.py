from . import views
from django.urls import path

urlpatterns = [
    path('', views.PlatformList.as_view(), name='home'),
    path('<slug:slug>/', views.platform_detail, name = 'platform_detail')
]