from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db import models
from .models import Platform
from .models import Game
from .forms import AddPlatformForm, AddGameForm


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
    # platform_form = AddPlatformForm()
    return render(
        request,
        "library/platform_detail.html",
        {"platform": platform, 
        "games": games},
    )


def add_platform(request):
    add_platform_form = AddPlatformForm()
    if request.method == 'POST':
         add_platform_form = AddPlatformForm(request.POST)
         if add_platform_form.is_valid():
            add_gameplatform_form.save()
            # Add any additional logic or redirect here
            return redirect('home')

    return render(request,
                  'library/add_platform.html',
                  {'add_platform_form': add_platform_form})

def add_game(request):
    add_game_form = AddGameForm()

    if request.method == 'POST':
        add_game_form  = AddGameForm(request.POST)
        if add_game_form.is_valid():
            add_game_form.save()
            # Add any additional logic or redirect here
            return redirect('home')

    return render(request,
                  'library/add_game_form.html',
                  {'add_game_form': add_game_form})

        