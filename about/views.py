from django.views import generic
from django.shortcuts import render
from .models import Bio

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