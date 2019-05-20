from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.conf import settings

from .models import Scrap

# Create your views here.

class ScrapList(ListView):

    model = Scrap
    context_object_name = 'scraps'

class ScrapDetail(DetailView):

    model = Scrap
    context_object_name = 'scrap'
