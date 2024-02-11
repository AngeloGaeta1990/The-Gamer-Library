from django.urls import path
from . import views


urlpatterns = [
    path('', views.bio, name='get_in_touch'),
    path('collaborate/', views.collaborate, name='collaborate'),
]
