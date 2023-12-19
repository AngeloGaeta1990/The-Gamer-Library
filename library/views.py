from django.shortcuts import render
from django.views import generic
from .models import Platform


# Create your views here.
class PlatformList(generic.ListView):
    queryset = Platform.objects.all()
    template_name = "platform_list.html"