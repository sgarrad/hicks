from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from braces.views import LoginRequiredMixin
from .models import Project, Definition, Term
from ..hicks_language.models import Language
from django.db.models import Prefetch


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ProjectLanguageView(LoginRequiredMixin, ListView):
    template_name = 'hicks_glossary/project_language.html'
    context_object_name = 'definitions'

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, slug=kwargs['project_slug'])
        self.target_language = get_object_or_404(Language, code=kwargs['language_code'])
        return super(ProjectLanguageView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = Definition.objects.filter(project=self.project)
        qs = qs.prefetch_related(Prefetch('terms', Term.objects.all().filter(language=self.target_language)))
        return qs

    def get_context_data(self, **kwargs):
        context = super(ProjectLanguageView, self).get_context_data(**kwargs)
        context.update({
            'project': self.project,
            'target_language': self.target_language
        })
        return context
