from django.shortcuts import render
from django.views import generic
from django.db import models
from .models import Platform
from. models import Game

# Create your views here.
class PlatformList(generic.ListView):
    context_object_name = 'platforms'
    template_name = "library/index.html"
    # paginate_by = 6

    def get_queryset(self):
        # Query all platform instances, including subclasses
        # return Platform.objects.all()
        return Platform.objects.annotate(game_count=models.Count('games_platform')).all()

        