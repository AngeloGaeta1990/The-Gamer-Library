from django.shortcuts import render
from django.views import generic
from .models import Platform


# Create your views here.
class PlatformList(generic.ListView):
    context_object_name = 'platforms'
    template_name = "library/index.html"

    def get_queryset(self):
        # Query all platform instances, including subclasses
        return Platform.objects.all()
