from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.db import models
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Platform, Game
from .forms import (AddPlatformForm, EditPlatformForm, AddGameForm,
                    EditPCPlatformForm, EditConsolePlatformForm,
                    EditServicePlatformForm, EditMobilePlatformForm,
                    EditGameForm, AddWishlistGameForm)


# Create your views here.
@method_decorator(login_required(login_url='accounts/login/'), name='dispatch')
class PlatformList(generic.ListView):
    context_object_name = 'platforms'
    template_name = "library/index.html"
    # paginate_by = 6

    def get_queryset(self):
        # Query all platform instances, including subclasses
        # return Platform.objects.all()
        return Platform.objects.filter(user=self.request.user).annotate(
            game_count=models.Count('games')).all()


def platform_detail(request, user_id, slug):
    """
    Display an individual :model:`library.Library`.

    **Context**

    ``Platform``
        An instance of :model:`library.Platform`.

    **Template:**

    :template:`library/platform_detail.html`
    """
    user = request.user
    queryset = Platform.objects.filter(user=user)
    platforms = queryset.filter(slug=slug)

    if platforms.exists():
        platform = platforms.first()
        games = platform.games.all()
        return render(
            request,
            "library/platform_detail.html",
            {"platform": platform, "games": games},
        )
    else:
        raise Http404("Platform not found")


@login_required
def add_platform(request):
    if request.method == 'POST':
        add_platform_form = AddPlatformForm(request.POST, request.FILES)
        if add_platform_form.is_valid():
            platform_name = add_platform_form.cleaned_data['name']
            if Platform.objects.filter(name=platform_name,
                                       user=request.user).exists():
                add_platform_form.add_error('name', 'This platform already'
                                            ' exists.')
            else:
                platform = add_platform_form.save(commit=False)
                platform.user = request.user
                platform.save()
                messages.add_message(request, messages.SUCCESS,
                                     'new platform added')
                return redirect('home')

    else:
        add_platform_form = AddPlatformForm()

    return render(request,
                  'library/add_platform.html',
                  {'add_platform_form': add_platform_form})


def edit_platform(request, user_id, slug):
    """
    view to edit comments
    """
    platform = get_object_or_404(Platform,  user_id=user_id, slug=slug)
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

    edit_platform_form = form_class(request.POST,
                                    request.FILES, instance=platform)

    if request.method == 'POST':

        if edit_platform_form.is_valid():
            edit_platform_form.save()
            messages.add_message(request, messages.SUCCESS, 'Platform edited!')
            return HttpResponseRedirect(reverse('home'))
    else:
        edit_platform_form = form_class(instance=platform)

    return render(request, 'library/edit_platform.html',
                  {'edit_platform_form': edit_platform_form,
                   'platform': platform})


def delete_platform(request, user_id, slug):
    """
    view to delete platform
    """
    platform = get_object_or_404(Platform,  slug=slug)
    platform.delete()
    messages.add_message(request, messages.SUCCESS, 'Platform deleted!')
    return HttpResponseRedirect(reverse('home'))


def add_game(request):
    add_game_form = AddGameForm(user=request.user)
    if request.method == 'POST':
        add_game_form = AddGameForm(request.user, request.POST, request.FILES)
        if add_game_form.is_valid():
            # TODO add videogames database API to get data and fill the form
            add_game_form.save()
            # Add any additional logic or redirect here
            return redirect('home')
        else:
            messages.error(request, 'Invalid form submission. Please check the'
                           ' form.')

    return render(request,
                  'library/add_game_form.html',
                  {'add_game_form': add_game_form})


def game_detail(request, user_id, platform_slug, game_slug):
    """
    Display an individual :model:`library.Game`.

    **Context**

    ``Game``
        An instance of :model:`library.Game`.

    **Template:**

    :template:`library/game_detail.html`
    """
    user = request.user
    platform = get_object_or_404(Platform, user=user, slug=platform_slug)
    game = get_object_or_404(Game, platform=platform, slug=game_slug)

    return render(
        request,
        "library/game_detail.html",
        {
         "platform": platform,
         "game": game},
    )


def edit_game(request, user_id, platform_slug, game_slug):
    """
    View to edit game
    """
    user = request.user
    platform = get_object_or_404(Platform, user=user, slug=platform_slug)
    game = get_object_or_404(Game, platform=platform, slug=game_slug)

    if request.method == 'POST':
        print("Platform Slug:", platform.slug)
        edit_game_form = EditGameForm(request.POST, request.FILES,
                                      instance=game)
        if edit_game_form.is_valid():
            edit_game_form.save()
            messages.success(request, 'Game edited!')
            return HttpResponseRedirect(reverse('game_detail', args=[user_id,
                                                platform.slug, game.slug]))
    else:
        edit_game_form = EditGameForm(instance=game)

    return render(request, 'library/edit_game.html', {
        'edit_game_form': edit_game_form,
        'platform': platform,
        'game': game,
    })


def delete_game(request, user_id, platform_slug, game_slug):
    """
    view to delete platform
    """
    user = request.user
    platform = get_object_or_404(Platform, user=user, slug=platform_slug)
    game = get_object_or_404(Game, platform=platform, slug=game_slug)
    if platform.user != user:
        return HttpResponseForbidden("You do not have permission to delete"
                                     " this game.")
    game.delete()
    messages.add_message(request, messages.SUCCESS, 'Game deleted!')
    return HttpResponseRedirect(reverse('home'))


def add_wishlist(request):
    add_wishlist_form = AddWishlistGameForm(user=request.user)
    if request.method == 'POST':
        add_wishlist_form = AddWishlistGameForm(request.user, request.POST,
                                                request.FILES)
        if add_wishlist_form.is_valid():
            # TODO add videogames database API to get data and fill the form
            add_wishlist_form.save()
            # Add any additional logic or redirect here
            return redirect('home')
        else:
            messages.error(request, 'Invalid form submission. Please check the'
                           ' form.')

    return render(request,
                  'library/add_wishlist_form.html',
                  {'add_game_form': add_wishlist_form})
