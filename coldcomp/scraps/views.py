from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404
from django.conf import settings

from .models import Scrap, Mood
from .forms import ScrapForm

# Create your views here.

class ScrapList(ListView):

    context_object_name = 'scraps'
    template_name = 'scrap_list.html'
    queryset = Scrap.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ScrapList, self).get_context_data(*args, **kwargs)
        context['mood'] = Mood.objects.all()
        return context

class ScrapDetail(DetailView):

    model = Scrap
    context_object_name = 'scrap'
    queryset = Scrap.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ScrapDetail, self).get_context_data(*args, **kwargs)
        context['mood'] = Mood.objects.all()
        return context

class ScrapCreate(LoginRequiredMixin, CreateView):
    template_name ='scraps/new.html'
    model = Scrap
    permission_required = 'scraps.can_add'
    form_class = ScrapForm
