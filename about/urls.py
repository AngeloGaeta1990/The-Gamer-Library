from django.urls import path
from . import views


urlpatterns = [
    path('', views.bio, name='about'),
    path('collaborate/', views.collaborate, name='collaborate'),
]
