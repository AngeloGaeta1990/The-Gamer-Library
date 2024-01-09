from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.db import models
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Platform
from .models import Game
from .forms import AddPlatformForm, EditPlatformForm, AddGameForm
from .forms import EditPCPlatformForm, EditConsolePlatformForm, EditServicePlatformForm, EditMobilePlatformForm, EditPlatformForm


# Create your views here.
class PlatformList(generic.ListView):
    context_object_name = 'platforms'
    template_name = "library/index.html"
    # paginate_by = 6

    def get_queryset(self):
        # Query all platform instances, including subclasses
        # return Platform.objects.all()
        return Platform.objects.annotate(game_count=models.Count('games')).all()

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
    games = platform.games.all()
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
            add_platform_form.save()
            # Add any additional logic or redirect here
            messages.add_message(
             request, messages.SUCCESS,
                'new platform added'
    )
            return redirect('home')

    return render(request,
                  'library/add_platform.html',
                  {'add_platform_form': add_platform_form})


def edit_platform(request, slug, platform_id):
    """
    view to edit comments
    """
    platform = get_object_or_404(Platform, pk=platform_id)
    if platform.category == 'pc':
        form_class = EditPCPlatformForm
    elif platform.category == 'console':
        form_class = EditConsolePlatformForm
    elif platform.category == 'service':
        form_class = EditServicePlatformForm
    elif platform.category == 'mobile':
        form_class = EditMobilePlatformForm
    else:
        form_class = EditPlatformForm

    edit_platform_form = form_class(data=request.POST, instance=platform)

    if request.method == 'POST':

        if dit_platform_form.is_valid():
            form.save()
    else:
          edit_platform_form = form_class(instance=platform)

    return render(request, 'library/edit_platform.html', {'edit_platform_form':edit_platform_form , 'platform': platform})

def delete_platform(request, slug, platform_id):
    """
    view to delete platform
    """
    platform = get_object_or_404(Platform, pk=platform_id)
    platform.delete()
    messages.add_message(request, messages.SUCCESS, 'Platform deleted!')
    return HttpResponseRedirect(reverse('platform_detail', args=[slug]))
    

def add_game(request):
    add_game_form = AddGameForm()

    if request.method == 'POST':
        add_game_form  = AddGameForm(request.POST)
        if add_game_form.is_valid():
            #TODO add videogames database API to get data and fill the form
            add_game_form.save()
            # Add any additional logic or redirect here
            return redirect('home')

    return render(request,
                  'library/add_game_form.html',
                  {'add_game_form': add_game_form})

        