from django.views.generic import ListView, DetailView

from braces.views import LoginRequiredMixin

from .models import Project, Definition, Term


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
