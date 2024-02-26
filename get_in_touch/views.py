from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .models import Bio
from .forms import CollaborateForm


def bio(request):
    """
    View function for rendering the bio page.

    **Context:**

    ``bio``
        An instance of :model:`your_app_name.Bio`.

    **Template:**

    :template:`get_in_touch/get_in_touch.html`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML response containing the 'get_in_touch.html'
        template with the retrieved 'bio' object.

    """
    bio = Bio.objects.all().order_by('-last_update').first()

    return render(
        request,
        "get_in_touch/get_in_touch.html",
        {"bio": bio},
    )


def collaborate(request):
    """
    View function for handling collaboration requests.

    **Context:**

    ``collaborate_form``
        An instance of :form:`your_app_name.CollaborateForm`.

    **Template:**

    :template:`get_in_touch/collaborate.html`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML response containing the 'collaborate.html'
        template with the collaboration form.

    """
    collaborate_form = CollaborateForm()
    if request.method == 'POST':
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS, 'collaboration request sent')
            return redirect('home')
    return render(request,
                  'get_in_touch/collaborate.html',
                  {'collaborate_form': collaborate_form})
