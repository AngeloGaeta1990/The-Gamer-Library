from django.shortcuts import render, get_object_or_404
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

def platform_detail(request, slug):
    """
    Display an individual :model:`libray.Library`.

    **Context**

    ``Platform``
        An instance of :model:`library.Platform`.

    **Template:**

    :template:`library/platform_detail.html`
    """
    queryset = Platform.objects.all()
    # queryset = Platform.objects.filter(category="pc")
    platform = get_object_or_404(queryset, slug=slug)
    games = platform.games_platform.all()
    return render(
        request,
        "library/platform_detail.html",
        {"platform": platform, "games": games},
    )
        