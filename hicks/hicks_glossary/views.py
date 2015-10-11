from django.views.generic import ListView, DetailView, View
from django.http import HttpResponse
from braces.views import LoginRequiredMixin
from .models import Project, Definition, Term


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ProjectLanguageView(View):
    def get(self, request, project_slug, language_code):
        return HttpResponse('{} - {}'.format(project_slug, language_code))
