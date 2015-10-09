from django.shortcuts import render
from django.views.generic import ListView, DetailView

from braces.views import LoginRequiredMixin

from .models import Language


class LangDetailView(LoginRequiredMixin, DetailView):
    model = Language
    slug_field = 'code'
    slug_url_kwarg = 'code'


class LangListView(LoginRequiredMixin, ListView):
    model = Language
