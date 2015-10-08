from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Language


class LangDetailView(DetailView):
    model = Language
    slug_field = 'code'
    slug_url_kwarg = 'code'


class LangListView(ListView):
    model = Language
