from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .models import Bio
from .forms import CollaborateForm


# Create your views here.
def bio(request):
    """
    Renders the About page
    """
    bio = Bio.objects.all().order_by('-last_update').first()

    return render(
        request,
        "about/about.html",
        {"bio": bio},
    )


def collaborate(request):
    """
    add collaboration form
    """
    collaborate_form = CollaborateForm()
    if request.method == 'POST':
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            # Add any additional logic or redirect here
            messages.add_message(
                request, messages.SUCCESS, 'collaboration request sent')
            return redirect('home')
    return render(request,
                  'about/collaborate.html',
                  {'collaborate_form': collaborate_form})
