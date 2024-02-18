from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Platform, Game, WishListGame
from .forms import (AddPlatformForm, EditPlatformForm, AddGameForm,
                    EditPCPlatformForm, EditConsolePlatformForm,
                    EditServicePlatformForm, EditMobilePlatformForm,
                    EditGameForm, AddWishlistGameForm, EditWishListGameForm)


@login_required(login_url='intro')
def platform_list(request):
    """
    List all platforms in the database.

    **Context**

    ``platforms``
        An instance of :model:`library.Platform`.

    **Template:**

    :template:`library/index.html`
    """
    platforms = Platform.objects.all().order_by("name")
    games = []
    for platform in platforms:
        games.extend(list(platform.games.all().order_by("name")))
    return render(request, 'library/index.html', {'platforms': platforms,
                                                  'games': games})


@login_required
def platform_detail(request, user_id, platform_id):
    """
    Display an individual :model:`library.Library`.

    **Context**

    ``Platform``
        An instance of :model:`library.Platform`.

    **Template:**

    :template:`library/platform_detail.html`
    """
    user = request.user
    platform = get_object_or_404(Platform, user=user, id=platform_id)
    games = platform.games.all().order_by("name")
    wishlist_games = platform.wishlist_games.all().order_by("priority")

    return render(
        request,
        "library/platform_detail.html",
        {"platform": platform,
         "games": games,
         "wishlist_games": wishlist_games},
    )


@login_required
def add_platform(request):
    """
    Add a new platform to the database.

    **Template:**

    :template:`library/add_platform_form.html`
    """
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
                  'library/add_platform_form.html',
                  {'add_platform_form': add_platform_form})


@login_required
def edit_platform(request, user_id, platform_id):
    """
    Edit an existing platform in the database.

    **Template:**

    :template:`library/edit_platform_form.html`
    """
    platform = get_object_or_404(Platform,  user_id=user_id, id=platform_id)
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

    return render(request, 'library/edit_platform_form.html',
                  {'edit_platform_form': edit_platform_form,
                   'platform': platform})


@login_required
def delete_platform(request, user_id, platform_id):
    """
    Delete an existing platform from the database.
    """
    platform = get_object_or_404(Platform, user=request.user, id=platform_id)
    if platform.user != request.user:
        return HttpResponseForbidden("You do not have permission to delete"
                                     " this platform.")
    platform.delete()
    messages.add_message(request, messages.SUCCESS, 'Platform deleted!')
    return HttpResponseRedirect(reverse('home'))


@login_required
def add_game(request):
    """
    Add a new game to the database.

    **Template:**

    :template:`library/add_game_form.html`
    """
    add_game_form = AddGameForm(user=request.user)
    if request.method == 'POST':
        add_game_form = AddGameForm(request.user, request.POST, request.FILES)
        if add_game_form.is_valid():
            add_game_form.save()
            return redirect('home')
        else:
            messages.error(request, 'Invalid form submission. Please check the'
                           ' form.')
    return render(request,
                  'library/add_game_form.html',
                  {'add_game_form': add_game_form})


@login_required
def game_detail(request, user_id, platform_id, game_id):
    """
    Display an individual :model:`library.Game`.

    **Context**

    ``Game``
        An instance of :model:`library.Game`.

    **Template:**

    :template:`library/game_detail.html`
    """
    user = request.user
    platform = get_object_or_404(Platform, user=user, id=platform_id)
    game = get_object_or_404(Game, platform=platform, id=game_id)

    return render(
        request,
        "library/game_detail.html",
        {
         "platform": platform,
         "game": game},
    )


@login_required
def edit_game(request, user_id, platform_id, game_id):
    """
    Edit an existing game in the database.

    **Template:**

    :template:`library/edit_game_form.html`
    """
    user = request.user
    platform = get_object_or_404(Platform, user=user, id=platform_id)
    game = get_object_or_404(Game, platform=platform, id=game_id)

    if request.method == 'POST':
        edit_game_form = EditGameForm(request.POST, request.FILES,
                                      instance=game)
        if edit_game_form.is_valid():
            edit_game_form.save()
            messages.success(request, 'Game edited!')
            return HttpResponseRedirect(reverse('game_detail', args=[user_id,
                                                platform.id, game.id]))
    else:
        edit_game_form = EditGameForm(instance=game)

    return render(request, 'library/edit_game_form.html', {
        'edit_game_form': edit_game_form,
        'platform': platform,
        'game': game,
    })


@login_required
def delete_game(request, user_id, platform_id, game_id):
    """
    Delete an existing game from the database.
    """
    user = request.user
    platform = get_object_or_404(Platform, user=user, id=platform_id)
    game = get_object_or_404(Game, platform=platform, id=game_id)
    if platform.user != user:
        return HttpResponseForbidden("You do not have permission to delete"
                                     " this game.")
    game.delete()
    messages.add_message(request, messages.SUCCESS, 'Game deleted!')
    return HttpResponseRedirect(reverse('home'))


@login_required
def add_wishlist(request):
    """
    Add a new game to the wishlist.

    **Template:**

    :template:`library/add_wishlist_form.html`
    """
    add_wishlist_form = AddWishlistGameForm(user=request.user)
    if request.method == 'POST':
        add_wishlist_form = AddWishlistGameForm(request.user, request.POST,
                                                request.FILES)
        if add_wishlist_form.is_valid():
            add_wishlist_form.save()
            return redirect('home')
        else:
            messages.error(request, 'Invalid form submission. Please check the'
                           ' form.')

    return render(request,
                  'library/add_wishlist_form.html',
                  {'add_game_form': add_wishlist_form})


@login_required
def wishlist_game_detail(request, user_id, platform_id, wishlist_game_id):
    """
    Display an individual :model:`library.WishListGame`.

    **Context**

    'wishlist_game'
        An instance of :model:`library.WishListGame`.

    **Template:**

    :template:`library/wishlist_game_detail.html`
    """
    user = request.user
    platform = get_object_or_404(Platform, user=user, id=platform_id)
    wishlist_game = get_object_or_404(WishListGame, platform=platform,
                                      id=wishlist_game_id)

    return render(
        request,
        "library/wishlist_game_detail.html",
        {"platform": platform,
         "wishlist_game": wishlist_game},
    )


@login_required
def edit_wishlist_game(request, user_id, platform_id, wishlist_game_id):
    """
    Edit an existing game in the wishlist.

    **Template:**

    :template:`library/edit_wishlist_game_form.html`
    """
    user = request.user
    platform = get_object_or_404(Platform, user=user, id=platform_id)
    wishlist_game = get_object_or_404(WishListGame, platform=platform,
                                      id=wishlist_game_id)

    if request.method == 'POST':
        edit_wishlist_game_form = EditWishListGameForm(request.POST,
                                                       request.FILES,
                                                       instance=wishlist_game)
        if edit_wishlist_game_form.is_valid():
            edit_wishlist_game_form.save()
            messages.success(request, 'Game in Wishlist edited!')
            return HttpResponseRedirect(reverse('wishlist_game_detail',
                                                args=[user_id, platform.id,
                                                      wishlist_game.id]))
    else:
        edit_wishlist_game_form = EditWishListGameForm(instance=wishlist_game)

    return render(request, 'library/edit_wishlist_game_form.html', {
        'edit_wishlist_game_form': edit_wishlist_game_form,
        'platform': platform,
        'wishlist_game': wishlist_game,
    })


@login_required
def delete_wishlist_game(request, user_id, platform_id, wishlist_game_id):
    """
    Delete an existing game from the wishlist.
    """
    user = request.user
    platform = get_object_or_404(Platform, user=user, id=platform_id)
    game = get_object_or_404(WishListGame, platform=platform,
                             id=wishlist_game_id)
    if platform.user != user:
        return HttpResponseForbidden("You do not have permission to delete"
                                     " this game in wishlist.")
    game.delete()
    messages.add_message(request, messages.SUCCESS, 'Game deleted from'
                         ' wishlist!')
    return HttpResponseRedirect(reverse('home'))


def intro(request):
    """
    Render the intro page.

    **Template:**

    :template:`library/intro.html`
    """
    return render(request, 'library/intro.html')


def info(request):
    """
    Render the info page.

    **Template:**

    :template:`library/info.html`
    """
    return render(request, 'library/info.html')
