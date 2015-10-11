from django.views.generic import ListView, DetailView, TemplateView
from braces.views import LoginRequiredMixin
from .models import Project, Definition, Term
from ..hicks_language.models import Language


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ProjectLanguageView(LoginRequiredMixin, TemplateView):
    template_name = 'hicks_glossary/project_language.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectLanguageView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(slug=kwargs['project_slug'])

        # Create a definition list that contains:
        # definition.definition : An individual definition
        # definition.source     : A list of terms that matches the base language
        # definition.target     : A a list of terms that match the provided language code
        definition_list = []
        for definition in context['project'].definitions.all():
            single_definition = dict()
            single_definition['definition'] = definition
            single_definition['source'] = definition.term_definition.filter(language=context['project'].base_language)
            single_definition['target'] = definition.term_definition.filter(
                language=Language.objects.get(code=kwargs['language_code']))
            definition_list.append(single_definition)

        context['definitions'] = definition_list
        return context
