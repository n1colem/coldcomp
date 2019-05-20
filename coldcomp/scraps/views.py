from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Scrap

# Create your views here.

class ScrapList(ListView):

    model = Scrap
    context_object_name = 'scraps'
