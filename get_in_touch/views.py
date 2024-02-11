from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .models import Bio
from .forms import CollaborateForm


# Create your views here.
def bio(request):
    """
    Renders the Get in touch page
    """
    bio = Bio.objects.all().order_by('-last_update').first()

    return render(
        request,
        "get_in_touch/get_in_touch.html",
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
                  'get_in_touch/collaborate.html',
                  {'collaborate_form': collaborate_form})
